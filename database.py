import json
import os
from datetime import datetime
from typing import List, Dict, Any

class ProposalDatabase:
    """Persistent JSON database for storing proposals with automatic saving/loading."""
    
    def __init__(self, db_file: str = "proposals.json"):
        self.db_file = db_file
        self.proposals: List[Dict[str, Any]] = []
        self.load_proposals()
    
    def load_proposals(self) -> None:
        """Load existing proposals from JSON file."""
        try:
            if os.path.exists(self.db_file):
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    self.proposals = json.load(f)
                print(f"Loaded {len(self.proposals)} existing proposals from {self.db_file}")
            else:
                print(f"No existing database found. Starting with empty database.")
                self.proposals = []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading database: {e}. Starting with empty database.")
            self.proposals = []
    
    def save_proposals(self) -> None:
        """Save current proposals to JSON file."""
        try:
            with open(self.db_file, 'w', encoding='utf-8') as f:
                json.dump(self.proposals, f, indent=2, ensure_ascii=False)
            print(f"Saved {len(self.proposals)} proposals to {self.db_file}")
        except IOError as e:
            print(f"Error saving database: {e}")
    
    def add_proposal(self, proposal_data: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new proposal and save to database."""
        # Add timestamp if not present
        if 'timestamp' not in proposal_data:
            proposal_data['timestamp'] = datetime.now().isoformat()
        
        # Add unique ID
        proposal_data['id'] = len(self.proposals) + 1
        
        # Add to memory
        self.proposals.append(proposal_data)
        
        # Save to file immediately
        self.save_proposals()
        
        print(f"Added proposal {proposal_data['id']}: {proposal_data['title']}")
        return proposal_data
    
    def get_all_proposals(self) -> List[Dict[str, Any]]:
        """Get all proposals."""
        return self.proposals
    
    def get_proposal_by_id(self, proposal_id: int) -> Dict[str, Any] | None:
        """Get a specific proposal by ID."""
        for proposal in self.proposals:
            if proposal.get('id') == proposal_id:
                return proposal
        return None
    
    def update_proposal(self, proposal_id: int, updates: Dict[str, Any]) -> Dict[str, Any] | None:
        """Update an existing proposal."""
        for i, proposal in enumerate(self.proposals):
            if proposal.get('id') == proposal_id:
                # Update fields
                proposal.update(updates)
                proposal['last_updated'] = datetime.now().isoformat()
                
                # Save to file
                self.save_proposals()
                
                print(f"Updated proposal {proposal_id}")
                return proposal
        return None
    
    def delete_proposal(self, proposal_id: int) -> bool:
        """Delete a proposal by ID."""
        for i, proposal in enumerate(self.proposals):
            if proposal.get('id') == proposal_id:
                deleted_proposal = self.proposals.pop(i)
                self.save_proposals()
                print(f"Deleted proposal {proposal_id}: {deleted_proposal['title']}")
                return True
        return False
    
    def search_proposals(self, query: str) -> List[Dict[str, Any]]:
        """Search proposals by title, description, or problem."""
        query = query.lower()
        results = []
        
        for proposal in self.proposals:
            if (query in proposal.get('title', '').lower() or
                query in proposal.get('description', '').lower() or
                query in proposal.get('problem', '').lower()):
                results.append(proposal)
        
        return results
    
    def get_proposals_by_status(self, status: str) -> List[Dict[str, Any]]:
        """Get proposals by status (if you add status field later)."""
        return [p for p in self.proposals if p.get('status') == status]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics."""
        total_proposals = len(self.proposals)
        total_investment = sum(float(p.get('investment', 0)) for p in self.proposals)
        
        # Count by month (if you want to track trends)
        monthly_counts = {}
        for proposal in self.proposals:
            try:
                date = datetime.fromisoformat(proposal['timestamp'])
                month_key = f"{date.year}-{date.month:02d}"
                monthly_counts[month_key] = monthly_counts.get(month_key, 0) + 1
            except (ValueError, KeyError):
                continue
        
        return {
            'total_proposals': total_proposals,
            'total_investment_btc': total_investment,
            'monthly_submissions': monthly_counts,
            'database_file': self.db_file,
            'last_updated': datetime.now().isoformat()
        }
    
    def backup_database(self, backup_file: str = None) -> str:
        """Create a backup of the current database."""
        if backup_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"proposals_backup_{timestamp}.json"
        
        try:
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(self.proposals, f, indent=2, ensure_ascii=False)
            print(f"Database backed up to {backup_file}")
            return backup_file
        except IOError as e:
            print(f"Error creating backup: {e}")
            return ""
    
    def clear_database(self) -> None:
        """Clear all proposals (use with caution!)."""
        self.proposals = []
        self.save_proposals()
        print("Database cleared")

# Global database instance
db = ProposalDatabase()
