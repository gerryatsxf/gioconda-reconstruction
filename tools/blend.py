import numpy as np


class Blend:
    
    def matrices(self,fg,bg):
    #     fg: is the foreground image. It is an NxM matrix with values in interval [0,1]
    #     A:  alpha index. float number in interval [0,1]. This indicates how visible is the background image relative to foreground image.
    #     bg: is the background image. It is an NxM matrix with values in interval [0,1]
        (mfg,nfg) = fg.shape
        (mbg,nbg) = bg.shape

        if mfg == mbg:
            m = mfg

        if nfg == nbg:
            n = nfg

        fgbool = np.array(fg,copy=True)
        fgbool[fgbool > 0] = 1

        diff = fgbool - bg
        diff[diff < 0] = 0

        T = diff+bg-(fgbool-fg)

        return T




blend = Blend()
