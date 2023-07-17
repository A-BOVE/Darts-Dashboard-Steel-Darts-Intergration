

#%%
import streamlit as st
from streamlit import experimental_rerun as rerun


#def calculate_c(a,b,c):
 #   c =+ 1
    
def main():
    st.title(":dart: Darts")
    if 'startscore' not in st.session_state:
        c = 501
        st.session_state.startscore = c
        st.session_state.startscore2 = c 
        st.session_state.startscore3 = c
        st.write ("Start score = ", c)

    
    players = st.radio("select the amount of players",('1 Player Game', '2 Player game', '3 Player game'))

    if players == '1 Player Game': 
        st.write()

        st.session_state.b1 = st.number_input("Gegooide score", 0, 180, step=1)

        next_round = st.button('Next Round')
    
        if st.session_state.b1 or next_round:
            if st.session_state.startscore-st.session_state.b1 < 0:
                st.write("No Score")
                st.write("the remeaning score =", st.session_state.startscore)
        
            if st.session_state.startscore-st.session_state.b1 > 0:
                st.session_state.startscore = st.session_state.startscore-st.session_state.b1
                st.write("the remeaning score =", st.session_state.startscore)
                del st.session_state[session_state.b1]
   
            if st.session_state.startscore-st.session_state.b1 == 0: 
                st.write ("You have  won a leg of Darts!!!")
                next_leg = st.button("Next Leg")
                if next_leg:
                    # Delete all the items in Session state
                    for key in st.session_state.keys():
                        del st.session_state[key]
                    st.write("Fill in a new score")

    #Two PLayer Game 
    if players == '2 Player game': 
        st.session_state.b1 = st.number_input("Gegooide score player 1", 0, 180, step=1)
        st.session_state.b2 = st.number_input("Gegooide score player 2 ", 0, 180, step=1)
        next_round = st.button('Next Round')
    
        if next_round:
            if st.session_state.startscore-st.session_state.b1 < 0 or st.session_state.startscore2-st.session_state.b2 < 0:
                st.write("No Score")
                st.write("the remeaning score =", st.session_state.startscore, st.session_state.startscore2 )
        
            if st.session_state.startscore-st.session_state.b1 > 0 or  st.session_state.startscore2-st.session_state.b2 > 0:
                st.session_state.startscore = st.session_state.startscore-st.session_state.b1
                st.session_state.startscore2 = st.session_state.startscore2-st.session_state.b2
                st.write("the remeaning score =", st.session_state.startscore, st.session_state.startscore2)
                del st.session_state[session_state.b1]
                del st.session_state[session_state.b2]
   
            if st.session_state.startscore-st.session_state.b1 == 0: 
                st.write (" Player 1 has won a leg of Darts!!!")
                next_leg1 = st.button("Next Leg")
                if next_leg1:
                    # Delete all the items in Session state
                    for key in st.session_state.keys():
                        del st.session_state[key]
                    st.write("Fill in a new score")

            if st.session_state.startscore2-st.session_state.b2 == 0: 
                st.write (" Player 2 has won a leg of Darts!!!")
                next_leg2 = st.button("Next Leg")
                if next_leg2:
                    # Delete all the items in Session state
                    for key in st.session_state.keys():
                        del st.session_state[key]
                    st.write("Fill in a new score")

    #Three PLayer Game 
    if players == '3 Player game': 
        st.session_state.b1 = st.number_input("Gegooide score player 1", 0, 180, step=1)
        st.session_state.b2 = st.number_input("Gegooide score player 2", 0, 180, step=1)
        st.session_state.b3 = st.number_input("Gegooide score player 3", 0, 180, step=1)
        next_round = st.button('Next Round')
    
        if next_round:
            if st.session_state.startscore-st.session_state.b1 < 0 or st.session_state.startscore2-st.session_state.b2 < 0 or st.session_state.startscore3 - st.session_state.b3 <0:
                st.write("No Score")
                st.write("the remeaning score =", st.session_state.startscore, st.session_state.startscore2, st.session_state.startscore3 )
        
            if st.session_state.startscore-st.session_state.b1 > 0 or  st.session_state.startscore2-st.session_state.b2 > 0 or st.session_state.startscore3 > st.session_state.b3:
                st.session_state.startscore = st.session_state.startscore-st.session_state.b1
                st.session_state.startscore2 = st.session_state.startscore2-st.session_state.b2
                st.session_state.startscore3 = st.session_state.startscore3-st.session_state.b3
                st.write("the remeaning score =", st.session_state.startscore, st.session_state.startscore2,st.session_state.startscore3)
                del st.session_state[session_state.b1]
                del st.session_state[session_state.b2]
                del st.session_state[session_state.b3]
   
            if st.session_state.startscore-st.session_state.b1 == 0: 
                st.write (" Player 1 has won a leg of Darts!!!")
                next_leg1 = st.button("Next Leg")
                if next_leg1:
                    # Delete all the items in Session state
                    for key in st.session_state.keys():
                        del st.session_state[key]
                    st.write("Fill in a new score")

            if st.session_state.startscore2-st.session_state.b2 == 0: 
                st.write (" Player 2 has won a leg of Darts!!!")
                next_leg2 = st.button("Next Leg")
                if next_leg2:
                    # Delete all the items in Session state
                    for key in st.session_state.keys():
                        del st.session_state[key]
                    st.write("Fill in a new score")

            if st.session_state.startscore3-st.session_state.b3 == 0: 
                st.write (" Player 3 has won a leg of Darts!!!")
                next_leg2 = st.button("Next Leg")
                if next_leg2:
                    # Delete all the items in Session state
                    for key in st.session_state.keys():
                        del st.session_state[key]
                    st.write("Fill in a new score")



    
if __name__ == '__main__':
    main()



# import streamlit as st

# st.title('Counter Example using Callbacks')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def increment_counter():
#     st.session_state.count += 1

# st.button('Increment', on_click=increment_counter)

# st.write('Count = ', st.session_state.count)




# # %%

# %%
