       ! fortran program
       program kalimera
           implicit none
           TYPE complex_number
               REAL :: real, imaginary
           END TYPE complex_number

           TYPE(complex_number) :: c1, c2

           print *, "Each complex number shoud be typed as two &
               &numbers"

      end program kalimera
