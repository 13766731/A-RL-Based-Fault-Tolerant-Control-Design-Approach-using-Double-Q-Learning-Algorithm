from utils import *

while loop_circle < 100:
    if loop_circle == 0:
        y_out[loop_circle] = CSTR_plant(1)
        error_mse[loop_circle] = (1 - y_out[loop_circle])**2
               
    else:
        if loop_circle <= 10:
                control_action = PID_controller(CSTR_plant,y_out[loop_circle])
                y_out[loop_circle] = CSTR_plant(control_action)
                error_mse[loop_circle] = (1 - y_out[loop_circle])**2
               
                

        if loop_circle > 10 and a==0:

              if abs(error)<= 0.2 and a==0 :
               
                control_action = PID_controller(CSTR_plant,y_out[loop_circle])
                y_out[loop_circle] = CSTR_plant(control_action)+fault
                error_mse[loop_circle] = (1 - y_out[loop_circle])**2
                
                
                
              else: 
                
                state = Enter_state(error)      
               
                # (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Q_Learning_Algorithm (fault,state,State,Reward,Policy,CSTR_plant,loop_circle,y_out,error_mse)
                # a=1
                (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Duble_Q_Learning(fault,state,State,Reward,Policy,CSTR_plant,loop_circle,y_out,error_mse)
                a=1
               # 
                mean_duble[ii]=loop_Q_Learning
                
        if loop_circle > 10 and a==1:
            y_out[loop_circle] = CSTR_plant(A) + fault
            error_mse[loop_circle] = (1 - y_out[loop_circle])**2

                   
    error =   1 - y_out[loop_circle]
    loop_circle += 1
   
   

    
##################################### PLOT ##############################

t=np.linspace(0,100,100)        
plt.figure(1)
plt.plot(t,y_out[0:100])  
mse = 0
for e in range(np.size(error_mse)):
    mse += error_mse[e]
MSE = mse / np.size(error_mse)
print('MSE is :   ')
print(MSE)
################################### save data for plotting ###################

# savetxt('PId_Q1.csv', y_out, delimiter=',')