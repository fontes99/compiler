class PrePro:
    
    def filter(self, exp):
        
        exp_final = ""

        i = 0
        j = 0

        while i < len(exp):
            if exp[i] == '/' and exp[i+1] == '*':
                i += 2
                j = i
            
                while j < len(exp):
                    if exp[j] == '/' and exp[j-1] == '*':
                        j += 1
                        i = j
                        break
                    else:
                        j += 1

            else:
                exp_final += exp[i]
                i += 1
        
        # if exp[i] != '/' and exp[i-1] != '*': exp_final += exp[i]

        return exp_final

prepro = PrePro()
print(prepro.filter('/*a*/1/*aasa*/+1'))
