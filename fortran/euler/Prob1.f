c234567890
      PROGRAM P1
      sum=0
      DO 23 i=1,999
        IF ((MOD(i,3).EQ.0).OR.(MOD(i,5).EQ.0)) SUM=SUM+I
  23  CONTINUE
      PRINT *, SUM
      STOP
      END
