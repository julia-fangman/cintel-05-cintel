# cintel-05-cintel   # Julia Fangman

## Shiny Live Data Dashboard

### Introduction
This repository contains a Python application built with Shiny for displaying real-time data in a dashboard format. The goal of this project is to demonstrate the visualization and presentation of live data in an accessible and useful manner. The application showcases real-time temperature readings from St. Joseph, Missouri in a dashboard layout, providing users with insights into temperature trends over time. 
https://github.com/julia-fangman/cintel-05-cintel/blob/main/app.py 

### Basic App Example
Before beginning with enhancements or variations, ensure the app has similar functionality to this basic example:
https://github.com/denisecase/cintel-05-cintel-basic 

### Features Overview: 
Displays real-time temperature readings in a dashboard format.
Utilizes a deque to store the most recent readings and presents them for analysis.
Implements online machine learning algorithms such as linear regression to predict trends.
Allows customization of the theme, colors, and layout for better engagement.
Offers options to change the subject domain, integrate live data into previous interactive apps, or explore continuous intelligence.

#### Enhanced Features
Data Storage and Management
Readings are stored in a deque and wrapped in a reactive value, allowing for efficient handling of constantly changing data.

#### Expanded UI Components
The app includes multiple UI components, such as displaying current date and time, current temperature, most recent readings in a dataframe, temperature box plot, and a chart with the current trend. Each component is rendered separately based on reactive calculations, providing a comprehensive overview of the data.

#### Interactive Visualizations
Utilizing Plotly Express, the app features interactive visualizations like the temperature box plot and the chart with the current trend. These visualizations enhance user engagement and provide deeper insights into the data. Additional libraries such as Pandas, Plotly Express, and scipy.stats are integrated to enhance the functionality and visualization capabilities of the app. These libraries enable advanced data analysis and visualization techniques.

#### Improved UI Styling
The UI components are styled using CSS classes and inline styles, improving readability and visual appeal. The layout is designed to provide a seamless user experience across different devices.
