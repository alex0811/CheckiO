import re

def checkio(text, words):
    words_list = list(filter(lambda x: len(x)>0, words.lower().split(' ')))
    cmpList = cmp_list(text, words_list)
    return re.sub(
            (re.escape('|'.join(cmpList if len(cmpList) > 0 else words_list))).replace('\|','|'), 
            lambda x: '<span>' + x.group() + '</span>' if len(x.group()) > 0 else '', 
            text, 
            flags=re.IGNORECASE)

def cmp_list(text, words_list):
    result = []
    for t in text.split(' '):
        location = 0
        length = 0
        for word in words_list:
            if word in t.lower(): 
                if set(list(t.lower())) == set(list(word)):
                        new_location = 0
                        new_length = len(t)
                else:
                        new_location = t.lower().index(word)
                        new_length = len(word)

                if location <= new_location <= location + length - 1:
                        result.remove(t[location:location+length])
                        new_end = new_location + new_length
                        length = max(length, new_end - location)
                        result.append(t[location:location+length])
                else:
                        location = t.lower().index(word)
                        length = len(word)
                        result.append(t[location:location+length])
    return result


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("This is only a text example for task example.", "example") == 
    "This is only a text <span>example</span> for task <span>example</span>."), "Simple test"

    assert (checkio("Python is a widely used high-level programming language.", "pyThoN") ==
            "<span>Python</span> is a widely used high-level programming language."), "Ignore letters cases, but keep original"

    assert (checkio("It is experiment for control groups with similar distributions.", "is im") ==
            "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."), "Several subwords"

    assert (checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") ==
            "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."), "two spaces"

    assert (checkio("Did you find anything?", "word space tree") ==
            "Did you find anything?"), "No comments"

    assert (checkio("Hello World! Or LOL", "hell world or lo") ==
            "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"), "Contain or intersect"
            
    checkio("123456789", "3 6")
    checkio("aaaa", "aa a")
    checkio("abcd", "z y x w v u t s r q p o n m l k j i h g f e d c b a")
    checkio("lmn", "z y x w v u t s r q p o n m l k j i h g f e d c b a")
    checkio("", "")
    checkio("Y0ejVFvAqaPPH1!qq!sx HY!fEDdmeiL0J!uhEp 8UW NB!M CDs1VnUWCZDG;wXEAhW8qrfDM8.KpB04JByCXR0iZv X .Cgeu6i2394OTH O.UTnJA0k2S3E.dNE8Btz0xuajeQnGAGBbp.hRItjkO?7Is70?9z,xtKSkeZNu1cy?BodNEvLGZTn08?Zwe!J8CXrc 62lwnhLJKOG?3VpR!qU9!Z8UAgP,bVddYCaTeMrQBuH RrOTWkgfEtJe!tLsg24Oo0PJ9hFEBzO0HtAY;UK50OrU0B7Oa,2K0gk4FQdJP!cDsqi?hx!48vpRb.L8DWqZoP3e; 6FkAM2Kdfvt;dZouv4.Lvol7vdyDIf0;nVYfl1yzV7w?V?qEDi9oG3e0.ahRVPUqh913 7kuDHOxZQ 1Afa2xLhYA zUPx hCLLOqBJ8VIjtliljfJXcd OWAy4zpm Jn!NiDj6Us Ou.Sce778W8;9VoH085MHOaU,Ha9Clob0wKcToJBDbmY,GI5CtlEIKwBOwxLI0mJqwEiQO3Dzg.yeGtlNmcRsYhMKSUVZovvTmEYHHvX8qj8OzEdkzQa?BT?FD?LkAxaZh!WQSgDzWeQmMqKrRFS1HZxE7Sj8ma5KS8F;UDLCGN,;aE7u5gr!YS2pXrf1MeDzHIQxG,i5c?.NQLb,QU?1eI!!9zz4NaMiUuhQAGds z8iZbRd!m4AalEpVZQWLsd?tZ62wMpP3CynHroeT.?ANoaEn,r92OLLW3!iXp.,BatUG56?BGltE2GtqlRJ 43.S 7tWqrtnE0pfBWGnijN?hlv896.9dYrLdGR5tq,Ad7x.eKjG!qjRJ;rbcmjcgNt8VvpZTthivaT?FGKt;Om5Er8kqf9GF?NPTyEZto6RRS;w WKZyi0zJ OqlQNFyK6V3RTg2KFFwL0R7Zj6FlWljWcG ZMH?DDZ;i F qy.0kMPhOmsqkFvj1ULulES1zLk9VrwWCgE?mjB9sQAadYxy4v?!VsP,fz.BgwpNJ.IEgSX8ufxO7o;X zTyn8URX1DhCgVEoQ;gNaSowcn?OExjY7071.docTvrg28KLEskH.fSc9db!B!cA?PToRmRFQieOJ5,b dpYp9zTx1mX8DVAkASOF WV,9UC a1aL97vszgxIXRDweJvnWNAA0bDvrUA20cEeJ0OL,RHT4RPXzs72dRBuuzN3YtqyFNF7s2zztFw.SWyCx pRquYobSbsE,Uj7g?E1huD6 .,d82dVMLO4.G,VnLDCj,.5QS nvBhvOI6rLjFCkix,.qrB36h,IYwu6x; QU,eTaMmJC!lc8XPE?,?QFmW38eOGpCSlUov3lXdHVipsgcPYyo1VQd6ZK8lClwNpZ5 TDV5u2Pw;PWz4nGdMD8kophwjApjgo5U.7nwIZ1 mab! mfmfghG. z pAZIzj60mQIaw!DdocV.O?D..OOjdGehrLVL0dqgo2xByZ6bkAfHMihgeW   QW;bB6DHe3H?sxrWopeehilOr.j,JSPBUwe8rrpw5jr0QnI3xENv21?bihiP?5E! ,DiB4HKzz5oQ,wlOu!TReqRq1t1hkr?xx2jTK8 9ejjRwOglNV Z!L0K!L4H2.ZohC6iQvD!e mYgB1pX!JErYfjwX;CW2Uhr5,zlDvZ7U g3lMX7hb5TXUhc5,CytZ8P;DqLwb83,962TezFduncT?cc;HAuezA1?H8sUxvt1 DKFdyoEFG8OU00xz meHEOxJqoVm.Ch2djP6GJbCVB31e.rxjs7?plYg7mU2p Yj1V7bRlWBgBxiO6Q!q?IrJmXPAUz9CGlaxGwhiC2uUo8PlScp7eWS!w2VYWmndbjrqmgBj2r8PnJhce M0T3tvTzPz rHCSJ;ZW;ANJDDUnJUJfES;l,!1?XcTF7GZP6!TCXAJvK1T8,s ,,u8;IzYKFaW P;W9xdXRwmR,XQypa,H!8VUEOAtRJ arkCEN2I;!PX 1O2EGYcv?xsRlLStetAaXK7?j1uEiw2wYiHydaX4X r0J! XsdWq,WAZLvFj!KfiI!1!b;4uN6tZad Yf1Koe.!.J.LzXsk1 rzfray7TyqyVv!PH.aM7JXXndFLbcO2YlgiuP3c8crq!oqlbyTzsEIenaHEbg1Qp5QIzM.2 PNQ4Cvy1W14a,ppMTX  zhWqTIlr5kWtRWdc J3FIxs.16dLZgapu3vjdK;BrSQ3vcDkLFL7d8cpKWMPdenDyebpkmZU!J;hezlFYZ31?oHfmhs1phWJacptah11fqkB3Pq9Gn749gwvhZ .eBCcjQJOh725dul15xni1huwkUJhcoP7erDtEwrbL 7,qK6U5cR8Bj;y9gcPeYdTwlQ2t3OwgzGtQRiPn,IsgZ? f5 TMg2R3OsZsdT7z9 rdRcRi2gs8h62qOq5,e6LRZeQRDp2ve!CJHYE7, BR l4LZG3IEqYBLV,Lo6A9WmBB,5;Vx0r30cEmNO; enxkuiuZar.RNmpbmW96fpuT mxy!bDhWeQZIhbnNmsl,k O3blJcycWV4y,4W26M.w iKAo7; EZuPu9?fp356 lNdhi6FIX ,?nJtCRa?C8,iJ Csesj.1e1BnwUybeF M;PYcoBeul sFbqfFiX.rZj4T3x8,WuwYbY8gV5IXQQFk7RA0Xn!cw3MvSwlApnSuHT .M.L89nAQlixtIo6opbC5dtcKIXTvmWAsAUVhmFZEIzC0DY9fmjhsb4AwoM4rqpc6wMRc5UqTJLB2K2TrSeUAJZJzXKj!YX4f;Ld4mBl;;8GJLOz bkrSobHEPhmX.Cgv;RBpOyf167!o.CGc?JoXUuk?NtRevAvpE;1 xXnFooFe6RyzeORjo8pieaHAn8VDA6 Z4VvgnMwHR7Gi.gFTf;0vAED0vON..bzDs;SjAd;83BsDR5rn;XAsftoPt8jljAzdRWuLwe1QfRYxVBId3x TuIdShkybLLCGRfDeb6oa R9,N PRN05JESpQAy7EIWhd8s,dbvzxMsDOu9deHKL5aqnJlw NtyhKwqz g9vc03YeEKHM9IYygr7Y.7T0OuUdsJtZwyUP6;bZv7TIgAd2FS6 rxbnmtEFzYS8O9eJLKLLEnE483KOI;x k3vcTzd!oiOzY2u9ukZrGsr802YBGDkeQo wbnEJ4unUnvZzqFH1dVzmGnEHk2ICMWzG1WE5oR3j8ZP?2JDCzttOUr qs.gqJ; XIkWf!zpZh5E0  NSBjRHxLEZsLiTYj,zD;pUc9r,dUHWu.I1xPf2oPy?kwtB8;ySCT5yLTc;5llI1MlUA9;KDa hdVbFZ9M?ZiFloDVXX2eC0ClAI3swflyhgIg,AK7SJlz;O.lkHS,d8 8Ed1cwSjjpZIx;IFt?HNQ,obdY;iGSNo6d5 uN1ojspj 73VHDUsbpNX9tW5siqIYi?0k3eKAV9gi6w9NRS L!f gAkW8vYmNgyNVOomdocH4VEVDrk1S,P6RGLwnv I1.n76ZC2n05wHjciwnbgKKxlBO0NHjQIbKXHSSCmHyr25LVH?Occlt!DN0JPyj?kT0wQUF3NUr7.hfB;.mD.jSqWg2a5FWytvU on.KU92YhJd6s;ZpTcyi7.ivL PP!!5;8KdOpTKFjnK0Ss0Oo;Nvb9Q8fk6tbh4dD9qTXdyqXwu6JN E.!juR,WqKL4fQKE5iv?3Nkk0EMoPYv;Vq9hOSTsIHd8V7D9PKLZWrcIZz3ZbU2Q3ZJx8iqRwKZpL0u;KCEj2Sk5bAH;kH,t;qAt galZyGS2UUZ QPe GV42jkkIVnA!FBWVU6pI?ASmhydtBAe92ICo.rA7hXLeNBTistksVU 2TZt7 kOFHqztH?sEabt v8SMGcjlkBhycSH!q0qwKC8VgQ5Jb87QPb.DoJMekwEeOlDi1LPcvPzEzfdK1p;0kdTQe6vKPqHA94Xd,ArGTgzqEfb6kQz5;8,E41T8yFI Hmw5 FJ9WnR!N.1wncn5j6sXP1R3Wkqw3rnv!5Mkp7 djUki 8l 1VXGUo25kipkurTUZD9svC;5nvOhpKyQzR;GYaFUwC?o9TLTA.;rQ?WPwPHRPiHCFD0uwf1hzw71K3YZ10Q 5bj;Z,1smLU6H nigA 3BKaKKgf2p9kOF?zDA7aPv,3jlMgDEj0J!Y;tnaW0wHg!6q GGhaABwOWHz23jK?YfNas2BRyEcYvo2OF4beva1PMc kRXb3mQTRdhFF0.SH1CphqoNYyC1sYC2bPkXs22n vA 5mzYAe8Wu1OIXO5WZ Tm6Sz8LXtMr8iEf1X2XtQS,Lr2 OcfErFx.!sqBZfrlbqJSb4CY;KbaqwTW AX1e6DD,dxRYb?pP5cLhkbWB1qrgi2u,LBcs9fS CMMAjGjzkKl GvVQht1Sj2xyU7In4nMrEY 2o51wr4kWufPXivuDGPmlzIHcaIU;D;b7lUEh;4JoP 0aEmvW?!Sp7jA?2.uihLabYq 0nl!23T8,odNOY?hLEwqs0KGtV;bTgv4Wg9Z,86mEVqmZJldORzzx6PsrsVJ2a?DVxUxrrw 81aAZAHEIE5gB4j;s MXDS Gfwh!QYtR4OCj1RozV;U0ZnOZL, 7ZUojZlRizdXs1,OmUep41.TbGz2N0O5Y,l?h.YsI5Lbmm8Gz,YRm0SO2VHqUvqchS,utkevoIXNwmXRuGbmVFEvbrryXe Vc9Udp0DnFBEIO jk7BzgJ2UT5VDrqFfoT7Fu u6LeKXqxUb5dLNmV2?0P?MKrZwQUaZukKz.CGkPdr p2D?0QaC oF7k,bgN6Hzg.?f039?l14mEGhpz2jCULTgOlt2PO4IijCuheuBMqI5TvKqZhGVyKCdmkHMNkHEaNWExTFNxcVR,4l?NL8CNiNGoT!L?FNiNVoTL.yTRSNA CQ2vf,ZuRa74fVhQMIMP7i3c6mHA2FCOadzt5D5FgCyG?EdumBIhiM?ky vf,J9ZLbEtcm", "jvfvaqa BIhiM?") 

