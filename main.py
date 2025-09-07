import sys

from api_request import *
from ui import *
from paket_xut import get_package_xut
from my_package import fetch_my_packages
from bebas_puas import get_package_bebas
from xtra_combo_mini import get_package_xcm
from spesial_for_you import get_package_sfy
from edukasi import get_package_edu
from xtra_combo_old import get_package_xco
from bonus_xcp import get_package_bxcp
from xcp_xcv import get_package_xcpv
from xcp_gift import get_package_xcpg
from bonus_prepaid import get_package_bp
from hotrod_baru import get_package_hb
from pilkada_damai import get_package_pd
from xl_reward import get_package_xr
from bundling import get_package_bun
from bonus_akrab import get_package_ba
from xtra_combo_flex import get_package_xcf
from paket_custom_family import get_packages_by_family
from auth_helper import AuthInstance

show_menu = True
def main():
    while True:
        active_user = AuthInstance.get_active_user()

        # Logged in
        if active_user is not None:
            balance = get_balance(AuthInstance.api_key, active_user["tokens"]["id_token"])
            balance_remaining = balance.get("remaining")
            balance_expired_at = balance.get("expired_at")
           
            show_main_menu(active_user["number"], balance_remaining, balance_expired_at)
            
            choice = input("Pilih menu: ")
            if choice == "1":
                selected_user_number = show_account_menu()
                if selected_user_number:
                    AuthInstance.set_active_user(selected_user_number)
                else:
                    print("No user selected or failed to load user.")
                continue
            elif choice == "2":
                fetch_my_packages()
                continue
            elif choice == "3":
                # XUT 
                packages = get_package_xut()
                
                show_package_menu(packages)
            elif choice == "4":
                # Bebas Puas
                packages = get_package_bebas()
                
                show_package_menu(packages)
            elif choice == "5":
                # Xtra Combo Mini
                packages = get_package_xcm()
                
                show_package_menu(packages)
            elif choice == "6":
                # Spesial For you
                packages = get_package_sfy()
                
                show_package_menu(packages)
            elif choice == "7":
                # Edukasi
                packages = get_package_edu()
                
                show_package_menu(packages)
            elif choice == "8":
                # Xtra Combo Old
                packages = get_package_xco()
                
                show_package_menu(packages)
            elif choice == "9":
                # Bonus XCP
                packages = get_package_bxcp()
                
                show_package_menu(packages)
            elif choice == "10":
                # XCP & XCV
                packages = get_package_xcpv()
                
                show_package_menu(packages)
            elif choice == "11":
                # Bonus Prepaid
                packages = get_package_bp()
                
                show_package_menu(packages)
            elif choice == "12":
                # Hotrod Baru
                packages = get_package_hb()
                
                show_package_menu(packages)
            elif choice == "13":
                # Pilkada Damai
                packages = get_package_pd()
                
                show_package_menu(packages)
            elif choice == "14":
                # XL Reward
                packages = get_package_xr()
                
                show_package_menu(packages)
            elif choice == "15":
                # Bundling
                packages = get_package_bun()
                
                show_package_menu(packages)
            elif choice == "16":
                # XCP Gift
                packages = get_package_xcpg()
                
                show_package_menu(packages)
            elif choice == "17":
                # Bonus Akrab
                packages = get_package_ba()
                
                show_package_menu(packages)
            elif choice == "18":
                # Xtra Combo Flex
                packages = get_package_xcf()
                
                show_package_menu(packages)
            elif choice == "19":
                family_code = input("Enter family code (or '99' to cancel): ")
                if family_code == "99":
                    continue
                get_packages_by_family(family_code)
            elif choice == "99":
                print("Exiting the application.")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                pause()
        else:
            # Not logged in
            selected_user_number = show_account_menu()
            if selected_user_number:
                AuthInstance.set_active_user(selected_user_number)
            else:
                print("No user selected or failed to load user.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting the application.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
