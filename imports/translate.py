from deep_translator import GoogleTranslator


def translate(text,num_cap):
    
    limit= 4000
    end=limit
    start =0


    numBucles = round(len(text)/limit)+1
    acumulador = []


    for i in range(0,numBucles):
        
        seccion = text[start:end]
        if(end>len(text)):
            seccion = text[start:len(text)]
        end=end+limit
        start = start+limit

        traductor = GoogleTranslator(source='en', target='es')
        traducido = traductor.translate(seccion)
        acumulador.append(f"{traducido}")


    final = "".join(acumulador)
    cap=[final,num_cap]
    return cap