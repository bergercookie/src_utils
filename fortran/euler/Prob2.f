c234567890
      PROGRAM P2
      INTEGER a,b,sum1,x
      sum1=2
      a=1
      b=2
 1    x=a+b
      a=b
      b=x
      IF (MOD(x,2).EQ.0) THEN
        sum1=sum1+x
      ENDIF
      IF (x.LE.4000000) GOTO 1
      WRITE(*,*) sum1
      STOP
      END
