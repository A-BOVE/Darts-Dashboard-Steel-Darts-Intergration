#%%
import streamlit as st
from streamlit import experimental_rerun as rerun
#Add  counter 
def clear_session_state():
    st.clear()
    
def main():
    st.title(":dart: Darts")
    if 'startscore' not in st.session_state:
        c = 501
        st.session_state.startscore = c
        st.session_state.startscore2 = c 
        st.session_state.startscore3 = c

    if 'Total_Turns' not in st.session_state:
        st.session_state.Total_Turns = 0 

    if 'Total_Score1'not in st.session_state:
         st.session_state.Total_Score1 = 0

    if 'Total_Score2'not in st.session_state:
         st.session_state.Total_Score2 = 0

    if 'Total_Score3'not in st.session_state:
         st.session_state.Total_Score3 = 0
    

    # 1 Player Game 
    if 'legs_won_1' not in st.session_state:   
        st.session_state.legs_won_1 = 0

    # 2 Player Game
    if 'legs_won_1_2' not in st.session_state:   
        st.session_state.legs_won_1_2 = 0

    if 'legs_won_2_2' not in st.session_state:  
        st.session_state.legs_won_2_2= 0


    # 3 Player game 
    if 'legs_won_1_3' not in st.session_state:   
        st.session_state.legs_won_1_3 = 0

    if 'legs_won_2_3' not in st.session_state:  
        st.session_state.legs_won_2_3= 0
    
    if 'legs_won_3' not in st.session_state:
        st.session_state.legs_won_3 = 0 

    
    players = st.radio("select the amount of players",('1 Player Game', '2 Player game', '3 Player game'))

    #Score that are impossible to throw: 
    impossible_scores = [163, 166, 169, 172, 173, 175, 175, 178, 179]
    
    #1 Player game LEG COUNTER WORKS 
    if players == '1 Player Game': 

        st.write("The player has won", st.session_state.legs_won_1, "Legs")
        
        st.session_state.b1 = st.number_input("Gegooide score", 0, 180, step=1)

        if st.session_state.b1 in impossible_scores:
            st.write("Score is Impossible! Select a different score")
            del st.session_state['b1']

        next_round = st.button('Next Round')
        
        if next_round:
            if st.session_state.startscore-st.session_state.b1 < 0:
                st.write("No Score")
                st.write("the remeaning score =", st.session_state.startscore)
        
            if st.session_state.startscore-st.session_state.b1 > 0:
                st.session_state.startscore = st.session_state.startscore-st.session_state.b1
                st.session_state.Total_Score1 += st.session_state.b1 
                st.session_state.Total_Turns += 1 
                st.write("The remeaning score =", st.session_state.startscore)
                st.write("Your Average score =", (st.session_state.Total_Score1/st.session_state.Total_Turns))
                del st.session_state['b1']
                         
   
            if st.session_state.startscore - st.session_state.b1 == 0: 
                st.write ("You have won a leg of Darts!!!")
                next_leg = st.button("Next Leg")
                st.session_state.legs_won_1 +=1 
                st.session_state.Total_Turns += 1 
                st.write("The player has won", st.session_state.legs_won_1, "Legs")
                del st.session_state['b1']
                del st.session_state['startscore']
                if next_leg:
                    st.write("Leg", (st.session_state.Total_Turns + 1))

                    
    #Two PLayer Game 
    if players == '2 Player game': 
        st.session_state.b1 = st.number_input("Gegooide score player 1", 0, 180, step=1)
        st.session_state.b2 = st.number_input("Gegooide score player 2 ", 0, 180, step=1)

        next_round = st.button('Next Round')

        if st.session_state.b1 in impossible_scores:
            st.write("Score is Impossible for Player 1! Select a different score")
            
            del st.session_state['b1']

        if st.session_state.b2 in impossible_scores:
            st.write("Score is Impossible for Player 2! Select a different score")
            del st.session_state['b2']

    
        if next_round:
            if st.session_state.startscore-st.session_state.b1 < 0 or st.session_state.startscore2-st.session_state.b2 < 0:
                st.write("No Score")
                st.write("the remeaning score =", st.session_state.startscore, st.session_state.startscore2)
        
            if st.session_state.startscore-st.session_state.b1 > 0 and st.session_state.startscore2-st.session_state.b2 > 0:

                st.session_state.Total_Score1 += st.session_state.b1 
                st.session_state.Total_Score2 += st.session_state.b2
                st.session_state.Total_Turns += 1 

                st.session_state.startscore = st.session_state.startscore-st.session_state.b1
                st.session_state.startscore2 = st.session_state.startscore2-st.session_state.b2
                st.write("the remeaning score =", st.session_state.startscore, st.session_state.startscore2)

                st.write("The Average score for Player 1 =", (st.session_state.Total_Score1/st.session_state.Total_Turns))
                st.write("The Average score for Player 2 =", (st.session_state.Total_Score2/st.session_state.Total_Turns))

                del st.session_state['b1']
                del st.session_state['b2']
                del st.session_state['b3']
   
            if st.session_state.startscore - st.session_state.b1 == 0: 
                st.write ("Player 1 has won a leg of Darts!!!")
                st.session_state.Total_Turns += 1 
                next_leg = st.button("Next Leg")

                st.session_state.Total_Score1 += st.session_state.b1 
                st.session_state.Total_Score2 += st.session_state.b2

                st.session_state.legs_won_1_2+=1 
                st.write("Player 1 has won", st.session_state.legs_won_1_2, "Legs")
                st.write("Player 2 has won", st.session_state.legs_won_2_2, "Legs")

                st.write("----------------------------------------------------------")

                st.write("The Average score for Player 1 =", (st.session_state.Total_Score1/st.session_state.Total_Turns))
                st.write("The Average score for Player 2 =", (st.session_state.Total_Score2/st.session_state.Total_Turns))

                del st.session_state['b1']
                del st.session_state['b2']
                del st.session_state['startscore']
                del st.session_state['startscore2']
           
                                
            if st.session_state.startscore2 - st.session_state.b2 == 0: 
                st.write ("Player W has won a leg of Darts!!!")
                st.session_state.Total_Turns += 1 

                st.session_state.Total_Score1 += st.session_state.b1 
                st.session_state.Total_Score2 += st.session_state.b2

                next_leg = st.button("Next Leg")
                st.session_state.legs_won_2_2 +=1 
                st.write("Player 1 has won", st.session_state.legs_won_1_2, "Legs")
                st.write("Player 2 has won", st.session_state.legs_won_2_2, "Legs")
                st.write("----------------------------------------------------------")

                st.write("The Average score for Player 1 =", (st.session_state.Total_Score1/st.session_state.Total_Turns))
                st.write("The Average score for Player 2 =", (st.session_state.Total_Score2/st.session_state.Total_Turns))


                del st.session_state['b1']
                del st.session_state['b2']
                del st.session_state['startscore']
                del st.session_state['startscore2']
              
                                    
                                                
    #Three PLayer Game 
    if players == '3 Player game': 
        st.session_state.b1 = st.number_input("Gegooide score player 1", 0, 180, step=1)
        st.session_state.b2 = st.number_input("Gegooide score player 2", 0, 180, step=1)
        st.session_state.b3 = st.number_input("Gegooide score player 3", 0, 180, step=1)
        next_round = st.button('Next Round')

        if st.session_state.b1 in impossible_scores:
            st.write("Score is Impossible for Player 1! Select a different score")
            
            del st.session_state['b1']

        if st.session_state.b2 in impossible_scores:
            st.write("Score is Impossible for Player 2! Select a different score")
            del st.session_state['b2']

        if st.session_state.b3 in impossible_scores:
            st.write("Score is Impossible for Player 3! Select a different score")
            del st.session_state['b3']
    
        if next_round:
            if st.session_state.startscore-st.session_state.b1 < 0 or st.session_state.startscore2-st.session_state.b2 < 0 or st.session_state.startscore3 - st.session_state.b3 <0:
                st.write("No Score")
                st.write("the remeaning score =", st.session_state.startscore, st.session_state.startscore2, st.session_state.startscore3 )
        
            if st.session_state.startscore-st.session_state.b1 > 0 and  st.session_state.startscore2-st.session_state.b2 > 0 and st.session_state.startscore3 > st.session_state.b3:

                st.session_state.Total_Turns += 1 

                st.session_state.Total_Score1 += st.session_state.b1 
                st.session_state.Total_Score2 += st.session_state.b2
                st.session_state.Total_Score3 += st.session_state.b3

                st.session_state.startscore = st.session_state.startscore-st.session_state.b1
                st.session_state.startscore2 = st.session_state.startscore2-st.session_state.b2
                st.session_state.startscore3 = st.session_state.startscore3-st.session_state.b3


                st.write("the remeaning score =", st.session_state.startscore, st.session_state.startscore2,st.session_state.startscore3)

                
                st.write("The Average score for Player 1 =", (st.session_state.Total_Score1/st.session_state.Total_Turns))
                st.write("The Average score for Player 2 =", (st.session_state.Total_Score2/st.session_state.Total_Turns))
                st.write("The Average score for Player 3 =", (st.session_state.Total_Score3/st.session_state.Total_Turns))
                del st.session_state[session_state.b1]
                del st.session_state[session_state.b2]
                del st.session_state[session_state.b3]
  
            if st.session_state.startscore - st.session_state.b1 == 0: 

                st.session_state.Total_Turns += 1 

                st.session_state.Total_Score1 += st.session_state.b1 
                st.session_state.Total_Score2 += st.session_state.b2
                st.session_state.Total_Score3 += st.session_state.b3

                st.write ("Player 1 has won a leg of Darts!!!")
                next_leg = st.button("Next Leg")
                st.session_state.legs_won_1_3 +=1 
                st.write("Player 1 has won", st.session_state.legs_won_1_3, "Legs")
                st.write("Player 2 has won", st.session_state.legs_won_2_3, "Legs")
                st.write("Player 3 has won", st.session_state.legs_won_3, "Legs") 


                st.write("----------------------------------------------------------")

                st.write("The Average score for Player 1 =", (st.session_state.Total_Score1/st.session_state.Total_Turns))
                st.write("The Average score for Player 2 =", (st.session_state.Total_Score2/st.session_state.Total_Turns))
                st.write("The Average score for Player 3 =", (st.session_state.Total_Score3/st.session_state.Total_Turns))

                if next_leg:
                    del st.session_state['b1']
                    del st.session_state['b2']
                    del st.session_state['b3']
                    del st.session_state['startscore']
                    del st.session_state['startscore2']
                    del st.session_state['startscore3']
                                # Delete all the items in Session state
                                
            if st.session_state.startscore2 - st.session_state.b2 == 0: 
                st.session_state.Total_Turns += 1 

                st.session_state.Total_Score1 += st.session_state.b1 
                st.session_state.Total_Score2 += st.session_state.b2
                st.session_state.Total_Score3 += st.session_state.b3

                st.write ("Player 2 has won a leg of Darts!!!")
                next_leg = st.button("Next Leg")
                st.session_state.legs_won_2_3 +=1 
                st.write("Player 1 has won", st.session_state.legs_won_1_3, "Legs")
                st.write("Player 2 has won", st.session_state.legs_won_2_3, "Legs")
                st.write("Player 3 has won", st.session_state.legs_won_3, "Legs") 


                st.write("----------------------------------------------------------")

                st.write("The Average score for Player 1 =", (st.session_state.Total_Score1/st.session_state.Total_Turns))
                st.write("The Average score for Player 2 =", (st.session_state.Total_Score2/st.session_state.Total_Turns))
                st.write("The Average score for Player 3 =", (st.session_state.Total_Score3/st.session_state.Total_Turns))

                if next_leg:
                    del st.session_state['b1']
                    del st.session_state['b2']
                    del st.session_state['b3']
                    del st.session_state['startscore']
                    del st.session_state['startscore2']
                    del st.session_state['startscore3']
                

                
            if st.session_state.startscore3 - st.session_state.b3 == 0: 
                st.write ("Player 3 has won a leg of Darts!!!")

                st.session_state.Total_Turns += 1 

                st.session_state.Total_Score1 += st.session_state.b1 
                st.session_state.Total_Score2 += st.session_state.b2
                st.session_state.Total_Score3 += st.session_state.b3

                next_leg = st.button("Next Leg")
                st.session_state.legs_won_3 += 1 

                st.write("Player 1 has won", st.session_state.legs_won_1_3, "Legs") 
                st.write("Player 2 has won", st.session_state.legs_won_2_3, "Legs")  
                st.write("Player 3 has won", st.session_state.legs_won_3, "Legs")  
                st.write("----------------------------------------------------------")

                st.write("The Average score for Player 1 =", (st.session_state.Total_Score1/st.session_state.Total_Turns))
                st.write("The Average score for Player 2 =", (st.session_state.Total_Score2/st.session_state.Total_Turns))
                st.write("The Average score for Player 3 =", (st.session_state.Total_Score3/st.session_state.Total_Turns))


                if next_leg:
                    del st.session_state['b1']
                    del st.session_state['b2']
                    del st.session_state['b3']
                    del st.session_state['startscore']
                    del st.session_state['startscore2']
                    del st.session_state['startscore3']

            

       
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
