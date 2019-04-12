var 
i,k:longint; 
slovo,itog,s:string; 
begin 
itog:=''; 
readln(slovo); 
for i:=1 to length(slovo) div 2 do 
insert(slovo[2*i]+slovo[2*i-1],itog,length(itog)div 2+1);
if length(slovo) mod 2 <> 0 then insert(slovo[2*i+1],itog, length(itog) div 2 +1);
writeln(itog) 
end.