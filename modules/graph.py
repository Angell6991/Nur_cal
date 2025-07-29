import  matplotlib.pyplot   as  plt
import  numpy   as  np

def plot(name_1, name_2, win_1, win_2 ,attack_1, attack_2, relaunch_1, relaunch_2, die_list_1, die_list_2, pro_die_1, pro_die_2 ):

    ###-----------building_the_inside_graphic_part-------------###
    fig, axs    =   plt.subplots(1, 2, figsize=(13, 4), facecolor="#1D1D1D")

    axs[0].scatter(
            die_list_1, [ round(pro_die_1[i]*100, 3) for i in range(len(pro_die_1)) ], 
            zorder=2, color="#ff00ff", s=20  
            )
    axs[1].scatter(
            die_list_2, [ round(pro_die_2[i]*100, 3) for i in range(len(pro_die_2)) ], 
            zorder=2, color="#ff00ff", s=20 
            )

    ###-------------parameters_for_axis_x_and_y----------------###
    axs[0].grid(True, linestyle="dashed", color="#696969", alpha=0.5, zorder=1)
    axs[0].set_facecolor("#353535")
    axs[0].set_xlabel("Blows to die", color="#5AEDA3")
    axs[0].set_ylabel("Probability (%)", color="#5AEDA3")
    axs[0].xaxis.label.set_color("#5AEDA3")
    axs[0].yaxis.label.set_color("#5AEDA3")
    axs[0].tick_params(axis="x", colors='#5AEDA3')
    axs[0].tick_params(axis="y", colors='#5AEDA3')
    axs[0].xaxis.label.set_size(13)
    axs[0].yaxis.label.set_size(13)  
    axs[0].set_xticks(die_list_1)
    axs[0].set_yticks([ round(pro_die_1[i]*100, 3) for i in range(len(pro_die_1)) ])
    axs[0].set_title(f"{name_1}", color="#5AEDA3", fontsize="15")
   
    axs[1].grid(True, linestyle="dashed", color="#696969", alpha=0.5, zorder=1)
    axs[1].set_facecolor("#353535")
    axs[1].set_xlabel("Blows to die", color="#5AEDA3")
    axs[1].set_ylabel("Probability (%)", color="#5AEDA3")
    axs[1].xaxis.label.set_color("#5AEDA3")
    axs[1].yaxis.label.set_color("#5AEDA3")
    axs[1].tick_params(axis="x", colors='#5AEDA3')
    axs[1].tick_params(axis="y", colors='#5AEDA3')
    axs[1].xaxis.label.set_size(13)
    axs[1].yaxis.label.set_size(13)  
    axs[1].set_xticks(die_list_2)
    axs[1].set_yticks([ round(pro_die_2[i]*100, 3) for i in range(len(pro_die_2)) ])
    axs[1].set_title(f"{name_2}", color="#5AEDA3", fontsize="15")
   
    axs[0].legend(
        [f"win: {round((1-win_1)*100,3)}% \n attack true: {round(attack_1*100, 3)}% \n relaunch: {round(relaunch_1*100, 3)}%"],
        fontsize=9, 
        loc="upper right", 
        facecolor="#1D1D1D",
        edgecolor="#000000"
    ).get_texts()[0].set_color("#f5f5f5")

    axs[1].legend(
        [f"win: {round((1-win_2)*100,3)}% \n attack true: {round(attack_2*100, 3)}% \n relaunch: {round(relaunch_2*100, 3)}%"],
        fontsize=9, 
        loc="upper right", 
        facecolor="#1D1D1D",
        edgecolor="#000000"
    ).get_texts()[0].set_color("#f5f5f5")


    plt.tight_layout() 
    ###--------------------show_graph--------------------------###
    return  plt.savefig("graph_1_vs_1.png", dpi=300, bbox_inches="tight")


