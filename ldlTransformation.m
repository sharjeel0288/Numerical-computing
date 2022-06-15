function x = LDLFact(A,b)
% A is a symmetric matrix
% factor A such that A=LDL^T with
% L a lower triangular matrix with 1 for all its diagonal entries
[n,m]=size(A); if n~=m | n<0 error(’A must be a square matrix’);
end
L = zeros(n,n); for i = 1:n
L(i,i)=1; end
D = zeros(n,1); for i=1:n
D(i)=A(i,i)-L(i,1:i-1).^2*D(1:i-1);
for j=i+1:n
L(j,i)=(A(j,i)-L(j,1:i-1).*L(i,1:i-1)*D(1:i-1))/D(i); end
end
% solve Ly=b, Dz=y, L^Tx=z z = zeros(n,1); y = zeros(n,1); x = zeros(n,1); % Ly=b y(1) = b(1); for i=2:n y(i) = b(i)-L(i,1:i-1)*y(1:i-1);
end
% Dz = y;
for i = 1:n
z(i)=y(i)/D(i);
end
% L^T x = z; x(n) = z(n); for i = n-1:-1:1 x(i) = z(i)-L(i+1:n,i)’*x(i+1:n);
end

function LDLSol 
A = hilb(5); 
b = A*ones(5,1); 
x = LDLFact(A,b); 
x 
end
