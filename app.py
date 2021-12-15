import streamlit as st
import os

import matplotlib.pyplot as plt
import pandas as pd



from multipage import save, MultiPage, start_app, clear_cache

start_app() #Clears the cache when the app is started

app = MultiPage()
app.start_button = "Let's go!"
# app.navbar_name = "Navigation"
# app.next_page_button = "Next Page"
# app.previous_page_button = "Previous Page"


def startpage():
    st.write('''
    # Understanding the Venezuelan Crisis
    ## Analysis of 20 years of news articles. 
    ''')

    st.markdown(
        """
     <style>
    .stApp {
      background-image: url("https://images.unsplash.com/photo-1621622633934-b910be06148d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3538&q=80,%s");
      background-size: cover;
    }
    </style>
        """,
        unsafe_allow_html=True
    )

    link = "[Let's begin the journey](http://github.com)"
    st.markdown(link, unsafe_allow_html=True)
    
    
    
    
    
    

# def app1(prev_vars): #First page
# 	if prev_vars != None:

# 		start_index = prev_vars  #Defines the start index for a selectbox (defined below) as the option previously chosen by the user
# 	else:
# 		start_index = 1 #Defines the start index for a selectbox (defined below) as 1

# 	st.button("Do nothing...")
# 	var1 = 10
# 	var2 = 5
# 	if st.button("Click here to save the variables..."):
# 		st.write("First number: " + str(var1))
# 		st.write('Second number: ' + str(var2))
# 		save(var_list=[var1, var2], name="App1", page_names=["App2", "App3"]) #Saves the variables to be used on the second and third pages.
# 		######

# 	#Shows how to set placeholders based on a selection
# 	new_var_list = ["This framework rocks!", "This framework is really cool!", "I really liked this framework!"]
# 	new_var = st.selectbox("Select an option: ", new_var_list, index=start_index) #Creates a selectbox in order to show how to keep the option chosen by the user even after he leaves the page...
# 	start_index = new_var_list.index(new_var)

# 	save([start_index], "placeholder1", ["App2", "App3"]) #Saves the variable "start_index" to be used again on the first page

# def app2(prev_vars): #Second page
# 	if type(prev_vars) is int: #Checks if the user saved the variables previously
# 		st.write("Ooops... You forgot to save the variables...")
# 		start_index = prev_vars
# 		save([start_index], "placeholder", ["App1"])

# 	else:
# 		start_index, var1, var2 = prev_vars #Reads the variables previously saved
# 		if st.button("Click here to sum the variables"):
# 			sum_var = var1+var2
# 			st.write(sum_var)
			
# 		if st.button("Click here to save a new variable"):
# 			var3 = 27
# 			st.write(var3)
# 			save(var_list=[var3], name="last_var", page_names=["App3"])
# 		save([start_index], "placeholder", ["App1"])



		#####

def app3(prev_vars): #Third page
	if type(prev_vars) is int: #Checks if the user saved the variables previously
		st.write("Ooops... You forgot to save the variables...")
		start_index = prev_vars
		save([start_index], "placeholder", ["App1"])
	else:
		try: #Checks if the user saved the last variable on the second page
			start_index, var1, var2, var3 = prev_vars
			if st.button("Click here to erase the last variable"):
				clear_cache(["last_var"]) #Erases the variables saved under the name "last_var"

			if st.button("Click here to multiply the variables"):
				st.write(var1*var2*var3)
			save([start_index], "placeholder", ["App1"])
		except:
			st.write("Ooops... You forgot to save the last variable...")
			start_index = prev_vars[0]
			save([start_index], "placeholder", ["App1"])

app.set_initial_page(startpage)
app.add_app("App1", app1) #Adds first page (app1) to the framework
app.add_app("App2", app2) #Adds second page (app2) to the framework
app.add_app("App3", app3) #Adds third page (app3) to the framework
app.run() #Runs the multipage app!


