c234567890
      PROGRAM Prob4
      M=0
      Larger=0
      DO 23 num1=100,999
        DO 24 num2=100,999
            M=num1*num2
            IF (M.LT.100000) THEN
                i1=MOD(M,10)
                i2=MOD(M,100)/10
                i3=MOD(M,1000)/100
                i4=MOD(M,10000)/1000
                i5=M/10000
                sum1=i1+i2*10+i3*100+i4*1000+i5*10000
                sum2=i5+i4*10+i3*100+i2*1000+i1*10000
                IF (sum1.EQ.sum2) THEN
                    IF (Larger.LT.M) THEN
                        Larger=M
                        n1=num1
                        n2=num2
                    ENDIF
                ENDIF
            ELSE
                i1=MOD(M,10)
                i2=MOD(M,100)/10
                i3=MOD(M,1000)/100
                i4=MOD(M,10000)/1000
                i5=MOD(M,100000)/10000
                i6=M/100000
                sum1=i1+i2*10+i3*100+i4*1000+i5*10000+i6*100000
                sum2=i6+i5*10+i4*100+i3*1000+i2*10000+i1*100000   
                IF (sum1.EQ.sum2) THEN
                    IF (Larger.LT.M) THEN
                        Larger=M
                        n1=num1
                        n2=num2
                    ENDIF
                ENDIF
            ENDIF
 24   CONTINUE
 23   CONTINUE
      PRINT *, n1,n2
      PRINT *, Larger
      STOP
      END
