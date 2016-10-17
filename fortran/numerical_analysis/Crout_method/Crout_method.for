c234567890
      program Lu_Decomposition
      implicit double precision (a-h,o-z)
      parameter (kdim=20)
      dimension a(kdim,kdim),b(kdim),aux(kdim),sol(kdim)
c
      open(1,file='matrix.dat')
      read(1,*)n
      do i=1,n
        read(1,*) (a(i,j),j=1,n),b(i)
      enddo
      close(1)
c
c     L and U matrices will be written over A
c     Crout : diagonal(U)=UNIT
      call crout(kdim,n,a)
c
      open(2,file='res_lu.dat')
        write(2,*)' L-matrix: '
            do k1=1,n
            write(2,'(6(1x,f10.5))')(a(k1,k2),k2=1,k1)
            enddo
        write(2,*)' U-matrix: (UNIT diagonal omitted)'
            do k1=1,n
            write(2,'(6(1x,f10.5))')(a(k1,k2),k2=k1+1,n)
            enddo
      close(2)
c
c     Solution - Step (1) :  L.AUX=b  --&gt;  find AUX
      aux(1)=b(1)/a(1,1)
      do i=2,n
        sum=0.d0
        do j=1,i-1
        sum=sum+a(i,j)*aux(j)
        enddo
      aux(i)=(b(i)-sum)/a(i,i)
      enddo
c
c     Solution - Step (2) :  U.SOL=AUX  --&gt;  find SOL
      sol(n)=aux(n)
      do i=n-1,1,-1
        sum=0.d0
        do j=n,i+1,-1
        sum=sum+a(i,j)*sol(j)
        enddo
      sol(i)=aux(i)-sum
      enddo
c
      open(1,file='solution.dat')
      do i=1,n
      write(1,*)i,sol(i)
      enddo
      close(1)
c
      stop
      end

      subroutine crout(kdim,n,a)
      implicit double precision (a-h,o-z)
      dimension a(kdim,kdim)
      eps=1.d-8
c
      do j=2,n
       a(1,j) = a(1,j) / a(1,1)
      enddo
c
      do k=2,n
        do i=k,n
         sum=0.d0
         do j=1,k-1
           sum=sum+a(i,j)*a(j,k)
         enddo
         a(i,k)=a(i,k)-sum
        enddo
c
        do j=k+1,n
         sum=0.d0
         do i=1,k-1
           sum=sum+a(k,i)*a(i,j)
         enddo
         a(k,j)=(a(k,j)-sum)/a(k,k)
        enddo
      enddo
c
      return
      end
