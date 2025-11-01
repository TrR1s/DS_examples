from subjects.player.player import TemplateForPool

ID_SET = set(range(100,1000))

low_plr_template = TemplateForPool(
            id_set= ID_SET,
            pool_depth = 40,
            ev = -0.02,
            std = 1.18,
            bet = 10,
            base_hand_amount =70,
            std_hand_amount = 12,
    
    )

low_ludoman_template = TemplateForPool(
            id_set= ID_SET,
            pool_depth = 30,
            ev = -0.027,
            std = 1.18,
            bet = 10,
            base_hand_amount =400,
            std_hand_amount = 40,
    
    )


silver_plr_template = TemplateForPool(
            id_set= ID_SET,
            pool_depth = 20,
            ev = -0.01,
            std = 1.3,
            bet = 35,
            base_hand_amount =100,
            std_hand_amount = 15,
    
    )

vip_plr_template = TemplateForPool(
            id_set= ID_SET,
            pool_depth = 9,
            ev = -0.007,
            std = 1.2,
            bet = 100,
            base_hand_amount =150,
            std_hand_amount = 30,
    
    )

cheet_plr_template = TemplateForPool(
            id_set= ID_SET,
            pool_depth = 1,
            ev = 0.15,
            std = 0.3,
            bet = 75,
            base_hand_amount =20,
            std_hand_amount = 2,
    
    )