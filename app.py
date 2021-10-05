import streamlit as st
import numpy as np
from functions import goodfood, bonappetit, nigella, olive

#Make a title

st.title("What's for dinner?")

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
        
        candidates = [c for c in candidates if c!=False]
        
        if len(candidates)==0:
            st.write('Whoops! Try a different source/ingredient combination')
        else:
            link = candidates[np.random.randint(0,len(candidates))]
        
            st.success("Here's your recipe: [link]("+link+")")
            st.balloons()
