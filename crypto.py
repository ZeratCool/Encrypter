from time import time
from pyfiglet import figlet_format
import AES_crypt, encode_64, shutil

class ZCryptoVisualizer:
    @staticmethod
    def visualize_progress(total_steps):
        for step in range(1, total_steps + 1):
            percentage = step / total_steps * 100
            bar_length = int(percentage / 2)
            bar = "#" * bar_length + "-" * (50 - bar_length)

            print(f"\r[{bar}] {percentage:.2f}%", end="")
            time.sleep(0.1)

        print("\nProcess complete!\n")

    def encrypt_visualization(self):
        print("Encrypting your files:")
        self.visualize_progress(20)

    def decrypt_visualization(self):
        print("Decrypting your files:")
        self.visualize_progress(20)






if __name__ == '__main__':
    intro = figlet_format("Z-Crypter", font='cybermedium')
    intro_result = f'''
    =======================================
    {intro}
    =======================================
    Welcome to the Crypter !!!
    '''
    key = input("[?] Enter Numeric Weak Key : ")
    path = input("[?] Enter Path of File : ")
    bypassVM = input("[?] Want to BypassVM (y/n): ")
    bypassVM = bypassVM.lower()

    print("\n[*] Making Backup ...")
    shutil.copyfile(path, path + ".bak")
    print("[+] Done !")

    print(f"\n[*] Initaiting Base64 Encryption Process ...")
    test2 = encode_64.Encode()
    test2.encode(path)
    print(f"[+] Operation Completed Successfully!\n")

    print("\n[*] Initiating AES Encryption Process ...")
    test1 = AES_crypt.Encryptor(key, path, bypassVM)
    test1.encrypt_file()
    print("[+] Process Completed Successfully!")