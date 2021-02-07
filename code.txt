#include<iostream>
#include<vector>
#include<string>

using namespace std;

struct Node
{
	int d;
	Node *n;

	Node(int data)
	{
		d = data;
		n = NULL;
	}
};

void display(Node *h)
{
	Node *start = h;

	while(start)
	{
		cout<<start->d<<" -> ";
		start = start->n;
	}
	cout<<"\n\n";
}

void swap_function (Node *node_1, Node *node_2)
{
	int temp = node_1->d;
	node_1->d = node_2 -> d;
	node_2 -> d = temp;
}

void bubble(Node *h)
{
	int swap;

	Node *left; 
	Node *right = NULL; 
	do{	
        swap = 0;
		left = h;
		while(left->n != right){
			if (left->d > left->n->d) {
				swap_function(left, left->n); 
                swap = 1; 
			}
			left = left->n;
		}right = left;
	}while(swap);
}

void selection(Node *h)
{
	int swap;

	Node *left; 
	Node *right = NULL; 
	do{	
        swap = 0;
		left = h;
		while(left->n != right){
			if (left->d > left->n->d) {
				swap_function(left, left->n); 
                swap = 1; 
			}
			left = left->n;
		}right = left;
	}while(swap);
}

void deleteNode(Node *nodeBefore)
{
    Node *temp;
    temp = nodeBefore->n;
    nodeBefore->n = temp->n;
    delete temp;
}

void delete_function(Node *head, int num)
{
    while(head->n){
        if (head->n->d == num)
        {
            deleteNode(head);
            return;
        }
        head = head->n;
    }
    cout<<"Number "<< num << " Not Found"<<endl; 
}

void menu()
{
    cout<<"Option 1: Add at beginning"<<endl;
    cout<<"Option 2: Add at End"<<endl;
    cout<<"Option 3: Add at Specific Position"<<endl;
    cout<<"Option 4: Delete Specific Value"<<endl;
    cout<<"Option 5: Display"<<endl;
    cout<<"Option 6: Selection Sort"<<endl;
    cout<<"Option 7: Bubble Sort"<<endl;
    cout<<"Option 9: Print Name and Roll Number"<<endl;
    cout<<"Option 0: Exit Program"<<endl<<endl;
}

void add_at_begin(Node *head, int num)
{
    Node *temp = new Node(1);
    temp->d = num;
    temp->n = head;
    head = temp;
    cout<<"head = "<<head->d<<endl;
}

void add_at_end(Node *head, Node *tail, int n)
{
    Node *tmp = new Node(n);
    tmp->d = n;
    tmp->n = NULL;

    if(head == NULL)
    {
        head = tmp;
        tail = tmp;
    }
    else
    {
        tail->n = tmp;
        tail = tail->n;
    }

}

int main()
{
	Node *h = new Node(2);
	h -> n = new Node(1);
	h -> n -> n = new Node(4);
	h -> n -> n -> n = new Node(3);
    Node *tail = h -> n -> n -> n ;

    menu();
    int option;
    cout<<"Select Option = ";
    cin>> option;
    while(1)
    {
        if(option == 0){
            break;
        }
        else if (option == 1){
            int num;
            cout<<" Input a Number ";
            cin>>num;
            add_at_begin(h, num);
        }
        else if (option == 2){
            int num;
            cout<<" Input a Number ";
            cin>>num;
            add_at_end(h, tail, num);
        }
        else if (option == 3){
            int num;
            cout<<" Input a Number ";
            cin>>num;
            cout<<" " <<endl;
        }
        else if (option == 4){
            int num;
            cout<<" Input a Number ";
            cin>>num;
            delete_function(h, num);
        }
        else if (option == 5){
            display(h);
        }
        else if (option == 6){
            bubble(h);
        }
        else if (option == 7){
            selection(h);
        }
        else if (option == 9){
            cout<<" Name " << " Roll Number "<<endl;
        }
        else {}
        
        cout<<"Select Option = ";
        cin>> option;
    }
    
	return 0;
}
