#!/usr/bin/env python3
"""
Database management script for Proposer.btc
Use this script to manage the JSON database, create backups, and view statistics.
"""

import sys
import os
from database import db

def show_help():
    """Show available commands."""
    print("""
Proposer.btc Database Management Script

Usage: python3 manage_db.py [command] [options]

Commands:
  list                    - List all proposals
  stats                   - Show database statistics
  backup [filename]       - Create database backup
  search <query>          - Search proposals
  view <id>              - View specific proposal
  clear                  - Clear all proposals (DANGEROUS!)
  help                   - Show this help message

Examples:
  python3 manage_db.py list
  python3 manage_db.py stats
  python3 manage_db.py backup my_backup.json
  python3 manage_db.py search "bitcoin"
  python3 manage_db.py view 1
""")

def list_proposals():
    """List all proposals in the database."""
    proposals = db.get_all_proposals()
    if not proposals:
        print("No proposals in database.")
        return
    
    print(f"\nFound {len(proposals)} proposals:\n")
    for proposal in proposals:
        print(f"ID: {proposal.get('id', 'N/A')}")
        print(f"Title: {proposal.get('title', 'N/A')}")
        print(f"Submitted: {proposal.get('timestamp', 'N/A')}")
        print(f"Investment: {proposal.get('investment', 'N/A')} BTC")
        print("-" * 50)

def show_stats():
    """Show database statistics."""
    stats = db.get_statistics()
    print("\nDatabase Statistics:")
    print(f"Total Proposals: {stats['total_proposals']}")
    print(f"Total Investment: {stats['total_investment_btc']} BTC")
    print(f"Database File: {stats['database_file']}")
    print(f"Last Updated: {stats['last_updated']}")
    
    if stats['monthly_submissions']:
        print("\nMonthly Submissions:")
        for month, count in sorted(stats['monthly_submissions'].items()):
            print(f"  {month}: {count} proposals")

def create_backup(filename=None):
    """Create a database backup."""
    backup_file = db.backup_database(filename)
    if backup_file:
        print(f"Backup created successfully: {backup_file}")
    else:
        print("Failed to create backup.")

def search_proposals(query):
    """Search proposals by query."""
    results = db.search_proposals(query)
    if not results:
        print(f"No proposals found matching '{query}'")
        return
    
    print(f"\nFound {len(results)} proposals matching '{query}':\n")
    for proposal in results:
        print(f"ID: {proposal.get('id', 'N/A')}")
        print(f"Title: {proposal.get('title', 'N/A')}")
        print(f"Description: {proposal.get('description', 'N/A')[:100]}...")
        print("-" * 50)

def view_proposal(proposal_id):
    """View a specific proposal by ID."""
    try:
        proposal_id = int(proposal_id)
    except ValueError:
        print("Invalid proposal ID. Must be a number.")
        return
    
    proposal = db.get_proposal_by_id(proposal_id)
    if not proposal:
        print(f"Proposal with ID {proposal_id} not found.")
        return
    
    print(f"\nProposal ID: {proposal['id']}")
    print(f"Title: {proposal.get('title', 'N/A')}")
    print(f"Subtitle: {proposal.get('subtitle', 'N/A')}")
    print(f"Description: {proposal.get('description', 'N/A')}")
    print(f"Problem: {proposal.get('problem', 'N/A')}")
    print(f"GitHub: {proposal.get('github', 'N/A')}")
    print(f"YouTube: {proposal.get('youtube', 'N/A')}")
    print(f"Email: {proposal.get('email', 'N/A')}")
    print(f"Website: {proposal.get('website', 'N/A')}")
    print(f"ETA: {proposal.get('eta', 'N/A')}")
    print(f"Investment: {proposal.get('investment', 'N/A')} BTC")
    print(f"Submitted: {proposal.get('timestamp', 'N/A')}")

def clear_database():
    """Clear all proposals (with confirmation)."""
    print("⚠️  WARNING: This will delete ALL proposals!")
    print("This action cannot be undone.")
    
    confirm = input("Type 'YES' to confirm: ")
    if confirm == 'YES':
        db.clear_database()
        print("Database cleared.")
    else:
        print("Operation cancelled.")

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'help':
        show_help()
    elif command == 'list':
        list_proposals()
    elif command == 'stats':
        show_stats()
    elif command == 'backup':
        filename = sys.argv[2] if len(sys.argv) > 2 else None
        create_backup(filename)
    elif command == 'search':
        if len(sys.argv) < 3:
            print("Error: Search query required.")
            print("Usage: python3 manage_db.py search <query>")
            return
        query = sys.argv[2]
        search_proposals(query)
    elif command == 'view':
        if len(sys.argv) < 3:
            print("Error: Proposal ID required.")
            print("Usage: python3 manage_db.py view <id>")
            return
        proposal_id = sys.argv[2]
        view_proposal(proposal_id)
    elif command == 'clear':
        clear_database()
    else:
        print(f"Unknown command: {command}")
        show_help()

if __name__ == '__main__':
    main()
