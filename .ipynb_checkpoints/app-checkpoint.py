import streamlit as st
import numpy as np
from functions import goodfood, bonappetit, nigella, olive, func_dict

#Make a title

st.title("What's for dinner?")

#Input form for user

form = st.form(key='input')
option = form.multiselect('Choose sources',['BBC Good Food','Bon Appetit','Nigella','Olive'])
ingredient = form.text_input(label="Give me a suggestion:")
submit_button = form.form_submit_button(label="Go")

#After submitting, get the links and randomly choose between them

if submit_button:
    with st.spinner(text='Searching...'):
    #If no websites are selected, ask for sources

        if len(option)==0:
            st.write('Please select some sources!')

    #For each source selected, func_dict returns appropriate scraping function and
    #appends returned candidate recipe to list

        else:
            candidates = []
            for op in option:

                try:
                    c = func_dict[op](ingredient)
                    candidates.append(c)
                except:
                    pass

        #Ask for a different combo if no recipes found

            if len(candidates)==0:
                st.write('Whoops, try a different source/ingredient combination')
            else:
                link = candidates[np.random.randint(0,len(candidates))]

                st.success("Here's your recipe: [link]("+link+")")
