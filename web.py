import streamlit as st
import functions

todos =functions.get_todos('to_dos.txt')

def add_todo():
    todo =st.session_state['new_todo']+ '\n'
    todos.append(todo)
    functions.write_todos('to_dos.txt',todos)
    

print(todos)
    
st.title('My to-do app')
st.subheader('I am going to have alot of fun with this.\n After I have to create my task tracker with deadlines')
for index,todo in enumerate(todos):
    click_key= 'click'+todo 
    checkbox = st.checkbox(todo, key=todo)
    clicked = st.button("Edit todo", key=click_key)
    if checkbox:
        todos.pop(index)
        functions.write_todos('to_dos.txt',todos)
        del st.session_state[todo]
        st.rerun() 
    #if clicked: clicking on the edit button to edit specific to-dos
        del st.session_state['new_todo']
        edit = st.session_state['new_todo']
        todos[index] = edit
        functions.write_todos('to_dos.txt',todos)
        st.session_state[click_key]
        del st.session_state['new_todo']
        st.rerun()

    #print (todo)
    
st.text_input(label='Enter another todo',placeholder=' e.g.clean your room...', key='new_todo', on_change=add_todo)