import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Función para cargar datos del archivo CSV
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'])  # Convertir la columna Date a tipo datetime si no lo está
    return df

# Función para obtener precios de cierre mensual de BTC desde un DataFrame
def get_btc_prices(df):
    # Seleccionar solo las columnas necesarias
    prices = df[['Date', 'Price']]
    prices.set_index('Date', inplace=True)  # Establecer Date como índice
    
    # Resample a precios mensuales
    monthly_prices = prices.resample('M').last()
    
    return monthly_prices

# Función para calcular DCA
def calculate_dca(start_date, end_date, monthly_investment, prices):
    # Filtrar los precios entre las fechas seleccionadas
    prices = prices[start_date:end_date]
    
    total_invested = 0
    total_btc = 0
    months_in_profit = 0
    months_in_loss = 0
    monthly_values = []
    previous_price = None

    for date, price in prices['Price'].items():
        total_invested += monthly_investment
        total_btc += monthly_investment / price

        current_value = total_btc * price
        monthly_values.append((date, total_invested, current_value))

        if previous_price is not None:
            if price > previous_price:
                months_in_profit += 1
            elif price < previous_price:
                months_in_loss += 1
        
        previous_price = price

    final_value = total_btc * prices['Price'].iloc[-1]
    profit_or_loss = final_value - total_invested
    pyr = (profit_or_loss / total_invested) * 100  # Calcular PYR

    return {
        'total_invested': total_invested,
        'current_value': final_value,
        'profit_or_loss': profit_or_loss,
        'pyr': pyr,  # Añadir PYR al resultado
        'months_in_profit': months_in_profit,
        'months_in_loss': months_in_loss,
        'monthly_values': monthly_values
    }

# Función para mostrar gráficos
def show_charts(result):
    dates, invested_values, current_values = zip(*result['monthly_values'])

    # Gráfico de la inversión vs. valor actual
    fig, ax = plt.subplots()
    ax.plot(dates, invested_values, label='Total Invested')
    ax.plot(dates, current_values, label='Current Value')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value (USD)')
    ax.set_title('Investment vs. Current Value Over Time')
    ax.legend()
    st.pyplot(fig)

    # Gráfico de profit/loss mensual
    monthly_profit_loss = [current - invested for invested, current in zip(invested_values, current_values)]
    fig, ax = plt.subplots()
    ax.bar(dates, monthly_profit_loss, color=['green' if x >= 0 else 'red' for x in monthly_profit_loss])
    ax.set_xlabel('Date')
    ax.set_ylabel('Profit/Loss (USD)')
    ax.set_title('Monthly Profit/Loss')
    st.pyplot(fig)

# Interfaz de usuario con Streamlit
def main():
    st.title('BTC DCA Simulator')
    
    st.write('Simulate Dollar-Cost Averaging (DCA) strategy for BTC investment using local CSV data.')

    csv_file = "Bitcoin Historical Data.csv"  # Nombre del archivo CSV en la raíz del proyecto

    # Cargar datos del archivo CSV
    df = load_data(csv_file)
    
    # Obtener los precios de cierre mensual del DataFrame cargado
    prices = get_btc_prices(df)
    
    with st.sidebar:
        # Formulario para ingresar fechas y monto de inversión mensual
        start_date = st.date_input('Start Date', value=df['Date'].min(), min_value=min(df['Date']), max_value=max(df['Date']))
        end_date = st.date_input('End Date', value=df['Date'].max(), min_value=min(df['Date']), max_value=max(df['Date']))
        monthly_investment = st.number_input('Monthly Investment (USD)', min_value=0.0)

        
        # Botón para calcular
        calculate_button = st.button('Calculate')
        
    if calculate_button:
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')

        # Calcular DCA con los precios filtrados
        result = calculate_dca(start_date_str, end_date_str, monthly_investment, prices)

        st.subheader('Results')
        st.write(f'Total Invested: ${result["total_invested"]:,.2f}')
        st.write(f'Current Value: ${result["current_value"]:,.2f}')
        st.write(f'Profit/Loss: ${result["profit_or_loss"]:,.2f}')
        st.write(f'PYR (Percent Yield Rate): {result["pyr"]:,.2f}%')
        st.write(f'Months in Profit: {result["months_in_profit"]}')
        st.write(f'Months in Loss: {result["months_in_loss"]}')

        # Mostrar gráficos
        show_charts(result)

if __name__ == '__main__':
    main()
