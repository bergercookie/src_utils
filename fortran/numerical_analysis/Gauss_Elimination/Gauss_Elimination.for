      implicit double precision (a-h,o-z)
      parameter (kdim=20)
      dimension a(kdim,kdim),b(kdim),x(kdim)
c
      open(1,file='matrix.dat')
      read(1,*)n
      do i=1,n
        read(1,*) (a(i,j),j=1,n),b(i)
      enddo
      close(1)
      call gauss(kdim,n,a,b,x)
      open(1,file='solution.dat')
      do i=1,n
      write(1,*)i,x(i)
      enddo
      close(1)
c
      stop
      end
c234567890

      subroutine gauss(kdim,n,a,b,x)
      implicit double precision (a-h,o-z)
      dimension a(kdim,kdim),b(kdim),x(kdim)
      eps=1.d-8
      do k=1,n-1
        if (dabs(a(k,k)).lt.eps)   stop   'Divide by Zero !!!!'
        do i=k+1,n 
           factor=a(i,k)/a(k,k)
           do j=k+1,n
           a(i,j)=a(i,j)-factor*a(k,j)
           enddo
           b(i)  =b(i)  -factor*b(k)
        enddo
      enddo
c
c-back substitution
      x(n)=b(n)/a(n,n)
      do i=n-1,1,-1
         sum=0.d0
         do j=i+1,n
           sum=sum+a(i,j)*x(j)
         enddo
         x(i)=(b(i)-sum)/a(i,i)
      enddo
c
      return
      end
