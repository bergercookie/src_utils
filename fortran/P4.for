c234567890
      program aekara
      read(*,*) a,b,c
      s=(a+b+c)/2
      area=sqrt(s*(s-a)*(s-b)*(s-c))
      print *, "area:",area
      end

