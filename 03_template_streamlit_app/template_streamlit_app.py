# Standard imports
import pandas as pd

# matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
#import seaborn as sns
#plotly
import plotly.express as px
import plotly.graph_objects as go

import streamlit as st

st.title("MPG")

df = pd.read_csv("mpg.csv")

# Basic set-up of the page:
# First the checkbox to show the data frame
if st.sidebar.checkbox('Show dataframe'):
    st.header("dataframe")
    st.dataframe(df.head())

# Then the radio botton for the plot type
show_plot = st.sidebar.radio(
    label='Choose Plot type', options=['Matplotlib', 'Plotly'])

st.header("Highway Fuel Efficiency")
years = ["All"]+sorted(pd.unique(df['year']))
year = st.sidebar.selectbox("choose a Year", years)   # Here the selection of the year.
car_classes = ['All'] + sorted(pd.unique(df['class']))
car_class = st.sidebar.selectbox("choose a Class", car_classes)  # and the selection of the class.

show_means = st.sidebar.radio(
    label='Show Class Means', options=['Yes', 'No'])

st.subheader(f'Fuel efficiency vs. engine displacement for {year}')


# With these functions we wrangle the data and plot it.
def mpg_mpl(year, car_class, show_means):
    fig, ax = plt.subplots()
    if year == 'All':
        group = df
    else:
        group = df[df['year'] == year]
    if car_class != 'All':
        st.text(f'plotting car class: {car_class}')
        group = group[group['class'] == car_class]
    group.plot('displ', 'hwy', marker='.', linestyle='', ms=12, alpha=0.5, ax=ax, legend=None)
    if show_means == "Yes":
      #  means = df.groupby('class').mean()
        means = df.groupby('class')[['displ', 'hwy']].mean()
        for cc in means.index:
            ax.plot(means.loc[cc, 'displ'], means.loc[cc, 'hwy'], marker='.', linestyle='', ms=12, alpha=1, label=cc)
        ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))
    ax.set_xlim([1, 8])
    ax.set_ylim([10, 50])
    plt.close()
    return fig


def mpg_plotly(year, car_class, show_means):
    if year == 'All':
        group = df
    else:
        group = df[df['year'] == year]
    if car_class != 'All':
        group = group[group['class'] == car_class]
    fig = px.scatter(group, x='displ', y='hwy', opacity=0.5, range_x=[1, 8], range_y=[10, 50])
    if show_means == "Yes":
      #  means = df.groupby('class').mean().reset_index()
        means = df.groupby('class')[['displ', 'hwy']].mean().reset_index()
        fig = px.scatter(means, x='displ', y='hwy', opacity=0.5, color='class', range_x=[1, 8], range_y=[10, 50])
        fig.add_trace(go.Scatter(x=group['displ'], y=group['hwy'], mode='markers', name=f'{year}_{car_class}',
                                 opacity=0.5, marker=dict(color="RoyalBlue")))
    return fig


if show_plot == 'Plotly':
    st.plotly_chart(mpg_plotly(year, car_class, show_means))

else:
    st.pyplot(mpg_mpl(year, car_class, show_means))

