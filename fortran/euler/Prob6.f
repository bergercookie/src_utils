c234567890
      PROGRAM Prob6
      INTEGER s1,s2,i,dif
      s1=0
      s2=0
      DO 23 i=1,100 !sum of the squares
        s1=s1+i**2
 23   CONTINUE
      DO 24 i=1,100 !square of the sums
        s2=s2+i
 24   CONTINUE
      s2=s2**2
      dif=s2-s1
      PRINT *,"Difference:", dif
      END
