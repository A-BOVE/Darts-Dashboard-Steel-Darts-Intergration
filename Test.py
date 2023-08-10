import streamlit as st 


def main():
    st.session_state.a = 0
    st.session_state.b= 0 

    if 'z' not in st.session_state.keys():

        st.session_state.z = 0
        
    button = st.button('Button')
    if button:
       st.session_state.z += 1
       st.session_state.a += 1
       st.session_state.b += 1
       del st.session_state['a']
       del st.session_state['b']
       st.write(st.session_state.z)



if __name__ == '__main__':
    main()
             
       
























