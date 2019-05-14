var 
   k,i:integer;
   slovar,slovo:string;
   
begin
slovar:='абвгдежзийклмнопрстуфхцчшщъыьэюя';

readln(k);
readln(slovo);
for i:=1 to length(slovo) do
   begin
      if pos(slovo[i],slovar)<>0 then
         begin
            if pos(slovo[i],slovar)-k<=0 then
               slovo[i]:=slovar[32-(k-pos(slovo[i],slovar))]
            else
               slovo[i]:=slovar[abs(pos(slovo[i],slovar)-k) mod 32];
   
         end;   
   end;
write(slovo);
end.