import streamlit as st
import numpy as np
from functions import goodfood, bonappetit, nigella, olive

#Make a title

st.title("Megan & Ollie's Meal Generator")

#Input form for user

form = st.form(key='input')
option = form.multiselect('Choose sources',['BBC Good Food','Bon Appetit','Nigella','Olive'])
ingredient = form.text_input(label="Give me a suggestion:")
submit_button = form.form_submit_button(label="Go")

#After submitting, get the links and randomly choose between them

if submit_button:
    
    if len(option)==0:
        st.write('Please select some sources!')
    
    else:

        candidates = []
        for op in option:
            if op=='BBC Good Food':
                candidates.append(goodfood(ingredient))
            if op=='Bon Appetit':
                candidates.append(bonappetit(ingredient))
            if op=='Nigella':
                candidates.append(nigella(ingredient))
            if op=='Olive':
                candidates.append(olive(ingredient))

        link = candidates[np.random.randint(0,len(candidates))]

        st.write("Here's your recipe: [link]("+link+")")
