class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = {"a":1,"b":3,"c":5,"d":7,"e":9,"f":11,"g":13,"h":15,
                    "i":17,"j":19,"k":21,"l":23,"m":25,"n":27,"o":29,
                    "p":31,"q":33,"r":35,"s":37,"t":39,"u":41,"v":43,
                    "w":45,"x":47,"y":49,"z":51}
        hm = {}
        
        for word in strs:
            letter_freq = ['a',0,'b',0,'c',0,'d',0,'e',0,'f',0,'g',0,'h',0,'i',0,'j',0,
                           'k',0,'l',0,'m',0,'n',0,'o',0,'p',0,'q',0,'r',0,'s',0,'t',0,
                           'u',0,'v',0,'w',0,'x',0,'y',0,'z',0]
            for letter in word:
                if letter in alphabet:
                    letter_freq[alphabet[letter]] += 1

            key = ''.join(str(count) for count in letter_freq)
            if key not in hm:
                hm[key] = [word]
            else:
                hm[key].append(word)
        return [sublst for sublst in hm.values()]