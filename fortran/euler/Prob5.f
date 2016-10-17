c234567890
      PROGRAM Prob5
      INTEGER number,i,j,flag
      number=0
      DO 23 i=2520,1000000000
        flag=1
        DO 24 j=1,20
            IF (MOD(i,j).NE.0) flag=0
 24     CONTINUE
        IF (flag.EQ.1) THEN
            number=i
            GOTO 25
        ENDIF
 23   CONTINUE
 25   PRINT *, number
      STOP
      END
