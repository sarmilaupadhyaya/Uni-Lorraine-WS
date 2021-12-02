import os
import sys
import decoder_jsgf as dj
import decoder_ngram as dn




def inference_set(files_directory, seq=None, extension=".raw", rule=None):
    """

    """
    skipped = 0
    filenames_decoded = dict()
    for root, dirs, files in os.walk(files_directory):
        for f in files:
            if f.endswith(".raw"):
                s = os.path.join(root, f)
                if rule == "ngram":
                    result = dn.inference(s)
                else:
                    result = dj.inference(s, rule)
                if result == "Skipped":
                    skipped += 1
                else:
                    filenames_decoded[s] = result
    return filenames_decoded



def generate_file(files_directory, speakers, rules, noises, result):
    """
    file that take each analysis parameter and returns the ref and generated file for wer

    """
    ref_pred_path = dict()
    for noise in noises:
        file_directory = os.path.join(files_directory, "SNR"+str(noise)+"dB")
        for speaker in speakers:
            for rule in rules:
                total = dict()
                files_path = os.path.join(file_directory, speaker)
                if rule not in  ["1digit","3digits","5digits"]:
                    for each in ["1digit_200","3digits_100","5digits_100"]:
                        files_path2 = os.path.join(files_path,"seq"+each+"_files" )
                        if os.path.isdir(files_path2):
                            total.update(inference_set(files_path2, rule= rule))
                        else:
                            sys.exit("the folder doesnt exist:" + files_path2)
                else:
                    rule_c = rule.replace("1digit", "1digit_200").replace("3digits", "3digits_100").replace("5digits", "5digits_100")
                    files_path2 = os.path.join(files_path,"seq"+rule_c+"_files" )
                    if os.path.isdir(files_path2):
                        total.update(inference_set(files_path2, rule= rule))
                    else:
                        import pdb
                        pdb.set_trace()
                        sys.exit("the folder doesnt exist:", files_path2)

                ref_path = result +"/ref_"+ noise + speaker + rule
                predicted = result+ "/pred_"+ noise + speaker + rule

                f = open(ref_path, "w")
                ff = open(predicted, "w")

                for each, value in total.items():
                    if value is None:
                        value="Not Found"
                    ref_path_v = each.replace(".raw",".ref")
                    ref_value = open(ref_path_v, "r").read().strip()
                    f.write(ref_value)
                    f.write("\n")
                    ff.write(value)
                    ff.write("\n")
                ref_pred_path[(speaker,rule, noise)] = list(zip(ref_path, predicted))
    return ref_pred_path



if __name__ == "__main__":
    filelists_path = sys.argv[1]
    speakers = sys.argv[2].strip().split(",")
    rules = sys.argv[3].strip().split(",")
    noise = sys.argv[4].strip().split(",")
    result = sys.argv[5]
    ref_path, pred_path = generate_file(filelists_path, speakers, rules, noise, result)
