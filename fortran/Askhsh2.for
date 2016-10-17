c234567890
      PROGRAM aekara
      REWIND(1)
      REWIND(2)
      REWIND(3)
      OPEN(unit=1,file='DATA1')
      OPEN(2,file='DATA2')
      READ(1,*) k1,k2,k3
      READ(2,*) r1,r2,r3
      ksum=k1+k2+k3
      IF(MOD(ksum,2).EQ.1) THEN
            OPEN(3,file='result2',STATUS='NEW')
            WRITE(3,*)(r1+r2+r3)
      ELSE
            WRITE(3,*) SQRT(FLOAT(ABS(k1*k2*k3)))
      ENDIF
      CLOSE(1)
      CLOSE(2)
      CLOSE(3,STATUS='KEEP')
      END
