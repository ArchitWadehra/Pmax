#from pvmodel_shaded import Panel
from gym_mppt.envs.pvmodel_shaded import Panel 

class Shaded2(object):
    def __init__(self):
        self.G = [100, 1000]  # read irradiance # Solar radiation in mW / sq.cm / Esto es la irradiancia para panel cuando [sombredo,sin_sombra]
        #self.T = 25  # read temperature # ojo con kelvin 273
        #self.SH = [4, 10, 7, 10, 10, 10]  # Shaded modules
        self.Mp = 10  # Modules in parallel
        self.Ng = [40, 38, 22]  # Parallel-connected series assemblies
        self.Iscr_sh = 0.375

    # def data(self, Irradiancia_maxima, T, V,SH):

    #     pv = Panel()

    #     IUN_i = pv.calc_pv(1000, T, V, 1)[0]
    #     print(V, IUN_i)

    #     if IUN_i < 0:
    #         IUN_i = 0
        
    #     VT = V
    #     PT = IUN_i*VT

    #     return IUN_i, VT, PT 

    # def data(self, Irradiancia_maxima, T, V,SH):

    #     pv = Panel()

    #     IUN_i = pv.calc_pv(1000, T, V, 4)[0]
    #     ISH_i = pv.calc_pv(100, T, V, 10)[0]
    #     print(V, IUN_i, ISH_i)

    #     if IUN_i < 0:
    #         IUN_i = 0
    #     if ISH_i < 0:
    #         ISH_i = 0

    #     I = max(IUN_i, ISH_i)
        
    #     VT = V
    #     PT = I*VT

    #     return I, VT, PT 

    def data(self, Irradiancia_maxima, T, V,SH):

        # G_ar = np.array(G) # Solar radiation in mW/sq.cm

        pv = Panel()
        # IUN = []
        # ISH = []
        Ipv = []

        for j in range(len(self.Ng)):
            # IUN_i = pv.calc_pv(Irradiancia_maxima, T, V, SH[j*2])[0] # asi estaria bien hecho, pero como dejamos fija la irradiancia maxima lo tomamos del self.G[1]
            IUN_i = pv.calc_pv(self.G[1], T, V, SH[j*2])[0]
            if IUN_i < 0:
                IUN_i = 0
            # IUN.append(IUN_i)
            ISH_i = pv.calc_pv(self.G[0], T, V, SH[j*2+1])[0]
            if ISH_i< 0:
                ISH_i = 0
            # ISH.append(ISH_i)
            Ipv.append(max(IUN_i, ISH_i))

        IT = Ipv[0] * self.Ng[0] + Ipv[1] * self.Ng[1] + Ipv[2] * self.Ng[2]
        VT = V
        PT = IT*VT
        return IT, VT, PT     

    # def data(self, Irradiancia_maxima, T, V,SH):

    #     # G_ar = np.array(G) # Solar radiation in mW/sq.cm

    #     pv = Panel()
    #     IUN = []
    #     ISH = []
    #     Ipv = []

    #     for j in range(len(self.Ng)):
    #         # IUN_i = pv.calc_pv(Irradiancia_maxima, T, V, SH[j*2])[0] # asi estaria bien hecho, pero como dejamos fija la irradiancia maxima lo tomamos del self.G[1]
    #         IUN_i = pv.calc_pv(self.G[1], T, V, SH[j*2])[0]
    #         if IUN_i < 0:
    #             IUN_i = 0
    #         IUN.append(IUN_i)
    #         ISH_i = pv.calc_pv(self.G[0], T, V, SH[j*2+1])[0]
    #         if ISH_i< 0:
    #             ISH_i = 0
    #         ISH.append(ISH_i)

    #     for jj in (range(len(self.Ng))):
    #         if IUN[jj] > self.Iscr_sh:
    #             Ipv.append(IUN[jj])
    #         else:
    #             Ipv.append(ISH[jj])

        
    #     IT = Ipv[0] * self.Ng[0] + Ipv[1] * self.Ng[1] + Ipv[2] * self.Ng[2]
    #     VT = V
    #     PT = IT*VT
    #     return IT, VT, PT 