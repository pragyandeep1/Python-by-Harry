st = "It's a string with double  spaces."
doublespace = st.find("  ")
print("Double space location: ",doublespace)
st = st.replace("  ", " ")
print(st)