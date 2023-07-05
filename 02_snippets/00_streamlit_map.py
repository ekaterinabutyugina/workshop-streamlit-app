# Sample Streamlit Map: https://docs.streamlit.io/library/api-reference/charts/st.map

st.subheader("Streamlit Map")
ds_geo = px.data.carshare()
print(ds_geo)
ds_geo['lat'] = ds_geo['centroid_lat']
ds_geo['lon'] = ds_geo['centroid_lon']
st.map(ds_geo)