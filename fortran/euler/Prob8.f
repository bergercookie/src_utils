c234567890
      PROGRAM Prob8
      INTEGER IARRAY(1000),i,m,p
c      DIMENSION IARRAY(1000)
      DO 23 i=1,10000
        READ(*,*) IARRAY(i)
 23   CONTINUE
c      READ *,IARRAY
      m=0
      p=1
      i=1
 25   DO 24 i=i,i+4
        p=p*IARRAY(i)
 24   CONTINUE
      IF (p.GT.m) THEN
        m=p
      ENDIF
      p=1
      IF (i.LT.997) GOTO 25
      PRINT *,'max=',m
      STOP
      END
