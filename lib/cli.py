from .models.organization import Organization
from .models.contributor import Contributor
from .models.contribution import Contribution
from .helpers import (
    display_menu, 
    get_int_input, 
    get_float_input, 
    get_date_input, 
    clear_screen, 
    print_success, 
    print_error, 
    print_warning
)

class CLI:
    """A command-line interface for the contributions management system."""
    
    def __init__(self):
        self.running = True

    def run(self):
        """Starts the main application loop."""
        while self.running:
            clear_screen()
            choice = display_menu("Main Menu", [
                "Manage Organizations",
                "Manage Contributors",
                "Manage Contributions",
                "View Reports",
                "Exit"
            ])

            if choice == 1:
                self.organization_menu()
            elif choice == 2:
                self.contributor_menu()
            elif choice == 3:
                self.contribution_menu()
            elif choice == 4:
                self.reports_menu()
            elif choice == 5:
                self.running = False
                print_success("Exiting application. Goodbye!")

    # --- Organization Management ---
    def organization_menu(self):
        """Manages the organization-related menu and actions."""
        while True:
            clear_screen()
            choice = display_menu("Organization Menu", [
                "Add New Organization",
                "View All Organizations",
                "Find Organization by ID",
                "Delete Organization",
                "Back to Main Menu"
            ])

            if choice == 1:
                name = input("Enter organization name: ")
                contact = input("Enter contact info: ")
                org = Organization.create(name, contact)
                print_success(f"Organization '{org.name}' created with ID {org.id}.")
            elif choice == 2:
                self.list_organizations()
            elif choice == 3:
                org_id = get_int_input("Enter organization ID: ")
                org = Organization.find_by_id(org_id)
                if org:
                    print(org)
                else:
                    print_error("Organization not found.")
            elif choice == 4:
                self.delete_organization()
            elif choice == 5:
                break
            input("\nPress Enter to continue...")

    def list_organizations(self):
        """Lists all organizations in the database."""
        organizations = Organization.get_all()
        if not organizations:
            print_warning("No organizations found.")
            return
        print("\n--- All Organizations ---")
        for org in organizations:
            print(f"ID: {org.id}, Name: {org.name}, Contact: {org.contact_info}")

    def delete_organization(self):
        """Handles the deletion of an organization."""
        self.list_organizations()
        org_id = get_int_input("Enter ID of organization to delete: ")
        if Organization.delete(org_id):
            print_success(f"Organization with ID {org_id} deleted successfully.")
        else:
            print_error("Organization not found.")

    # --- Contributor Management ---
    def contributor_menu(self):
        """Manages the contributor-related menu and actions."""
        while True:
            clear_screen()
            choice = display_menu("Contributor Menu", [
                "Add New Contributor",
                "View All Contributors",
                "Find Contributor by ID",
                "Find Contributor by Name",
                "Find Contributor by Type",
                "Update Contributor Target Amount",
                "Delete Contributor",
                "Back to Main Menu"
            ])

            if choice == 1:
                self.add_contributor()
            elif choice == 2:
                self.list_contributors()
            elif choice == 3:
                cont_id = get_int_input("Enter contributor ID: ")
                cont = Contributor.find_by_id(cont_id)
                if cont:
                    print(cont)
                else:
                    print_error("Contributor not found.")
            elif choice == 4:
                first = input("Enter first name: ")
                last = input("Enter last name: ")
                cont = Contributor.find_by_name(first, last)
                if cont:
                    print(cont)
                else:
                    print_error("Contributor not found.")
            elif choice == 5:
                cont_type = input("Enter contributor type ('member', 'volunteer', 'donor'): ")
                contributors = Contributor.find_by_type(cont_type)
                if contributors:
                    for cont in contributors:
                        print(cont)
                else:
                    print_warning("No contributors found for this type.")
            elif choice == 6:
                self.update_contributor_target()
            elif choice == 7:
                self.delete_contributor()
            elif choice == 8:
                break
            input("\nPress Enter to continue...")

    def add_contributor(self):
        """Handles the addition of a new contributor."""
        first = input("Enter first name: ")
        last = input("Enter last name: ")
        contact = input("Enter contact info: ")
        cont_type = input("Enter type ('member', 'volunteer', 'donor'): ")
        
        self.list_organizations()
        org_id = get_int_input("Enter organization ID for this contributor: ")
        target_amount = get_float_input("Enter target contribution amount (optional, defaults to 0): ", min_val=0)
        
        try:
            cont = Contributor.create(first, last, contact, cont_type, org_id, target_amount)
            print_success(f"Contributor '{cont.full_name}' created with ID {cont.id}.")
        except ValueError as e:
            print_error(f"Error creating contributor: {e}")

    def list_contributors(self):
        """Lists all contributors with their details, including progress."""
        contributors = Contributor.get_all()
        if not contributors:
            print_warning("No contributors found.")
            return
        print("\n--- All Contributors ---")
        for cont in contributors:
            print(f"ID: {cont.id}, Name: {cont.full_name}, Type: {cont.type}")
            print(f"  Target: ${cont.target_amount:.2f}, Total Contributions: ${cont.total_contributions:.2f}")
            print(f"  Progress: {cont.progress_percentage:.2f}%")
    
    def update_contributor_target(self):
        """Updates the target contribution amount for a contributor."""
        self.list_contributors()
        cont_id = get_int_input("Enter ID of contributor to update: ")
        new_target = get_float_input("Enter new target amount: ", min_val=0)
        
        if Contributor.update_target_amount(cont_id, new_target):
            print_success("Target amount updated successfully.")
        else:
            print_error("Contributor not found.")

    def delete_contributor(self):
        """Handles the deletion of a contributor."""
        self.list_contributors()
        cont_id = get_int_input("Enter ID of contributor to delete: ")
        if Contributor.delete(cont_id):
            print_success(f"Contributor with ID {cont_id} deleted successfully.")
        else:
            print_error("Contributor not found.")

    # --- Contribution Management ---
    def contribution_menu(self):
        """Manages the contribution-related menu and actions."""
        while True:
            clear_screen()
            choice = display_menu("Contribution Menu", [
                "Record a New Contribution",
                "View All Contributions",
                "Find Contributions by Contributor",
                "Find Contributions by Date Range",
                "Delete Contribution",
                "Back to Main Menu"
            ])

            if choice == 1:
                self.record_contribution()
            elif choice == 2:
                self.list_contributions()
            elif choice == 3:
                self.find_contributions_by_contributor()
            elif choice == 4:
                self.find_contributions_by_date_range()
            elif choice == 5:
                self.delete_contribution()
            elif choice == 6:
                break
            input("\nPress Enter to continue...")

    def record_contribution(self):
        """Handles the recording of a new contribution."""
        self.list_contributors()
        cont_id = get_int_input("Enter contributor ID: ")
        amount = get_float_input("Enter contribution amount: ", min_val=0.01)
        notes = input("Enter notes (optional): ")
        
        try:
            contribution = Contribution.create(amount, cont_id, notes)
            print_success(f"Contribution of ${contribution.amount:.2f} recorded for Contributor {cont_id}.")
        except ValueError as e:
            print_error(f"Error recording contribution: {e}")

    def list_contributions(self):
        """Lists all contributions in the database."""
        contributions = Contribution.get_all()
        if not contributions:
            print_warning("No contributions found.")
            return
        print("\n--- All Contributions ---")
        for c in contributions:
            print(f"ID: {c.id}, Amount: ${c.amount:.2f}, Date: {c.date}, Contributor ID: {c.contributor_id}")

    def find_contributions_by_contributor(self):
        """Finds and lists contributions for a specific contributor."""
        self.list_contributors()
        cont_id = get_int_input("Enter contributor ID: ")
        contributions = Contribution.find_by_contributor(cont_id)
        if contributions:
            print(f"--- Contributions for Contributor {cont_id} ---")
            for c in contributions:
                print(f"ID: {c.id}, Amount: ${c.amount:.2f}, Date: {c.date}, Notes: {c.notes}")
        else:
            print_warning("No contributions found for this contributor.")

    def find_contributions_by_date_range(self):
        """Finds and lists contributions within a date range."""
        print("Enter start date.")
        start_date = get_date_input()
        print("Enter end date.")
        end_date = get_date_input()
        
        contributions = Contribution.find_by_date_range(start_date, end_date)
        if contributions:
            print(f"--- Contributions from {start_date} to {end_date} ---")
            for c in contributions:
                print(f"ID: {c.id}, Amount: ${c.amount:.2f}, Date: {c.date}, Contributor ID: {c.contributor_id}")
        else:
            print_warning("No contributions found in this date range.")

    def delete_contribution(self):
        """Handles the deletion of a contribution."""
        self.list_contributions()
        cont_id = get_int_input("Enter ID of contribution to delete: ")
        if Contribution.delete(cont_id):
            print_success(f"Contribution with ID {cont_id} deleted successfully.")
        else:
            print_error("Contribution not found.")

    # --- Reports Menu ---
    def reports_menu(self):
        """Displays a menu for viewing various reports."""
        while True:
            clear_screen()
            choice = display_menu("Reports Menu", [
                "Contributor Progress Report",
                "Back to Main Menu"
            ])
            if choice == 1:
                self.show_contributor_progress_report()
            elif choice == 2:
                break
            input("\nPress Enter to continue...")

    def show_contributor_progress_report(self):
        """Generates and displays a report on contributor progress towards their target."""
        contributors = Contributor.get_all()
        if not contributors:
            print_warning("No contributors found to generate report.")
            return

        print("\n--- Contributor Progress Report ---")
        print("{:<25} {:<15} {:<15} {:<15}".format("Name", "Total Contrib.", "Target", "Progress %"))
        print("-" * 70)
        for cont in contributors:
            print(
                "{:<25} ${:<14.2f} ${:<14.2f} {:<15.2f}".format(
                    cont.full_name, 
                    cont.total_contributions, 
                    cont.target_amount, 
                    cont.progress_percentage
                )
            )