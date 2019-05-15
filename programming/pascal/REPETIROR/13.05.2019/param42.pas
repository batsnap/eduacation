var
    s:string;
function CompressStr(var s:string):string;
    var
        i,k,j:integer;
        c,itog,k1:string;
        
    begin
        s:=s+' ';
        c:=s[1];
        k:=1;
        itog:='';
        for i:=2 to length(s) do
            begin
                if s[i]=c then
                    k+=1;
                if (s[i]<>c) or (i=length(s)) then
                    begin
                        if k>3 then
                            begin
                                str(k,k1);
                                itog:=itog+c+'{'+k1+'}';
                            end
                        else
                            for  j:=1 to k do
                                itog:=itog+c;
                        c:=s[i];
                        k:=1;
                    end;
            end;
        CompressStr:=itog;
    end;
begin
    readln(s);
    writeln(CompressStr(s));
end.