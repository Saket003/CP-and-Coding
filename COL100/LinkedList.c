#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Node
{
    int data;
    struct Node* next;
};

// create a node with data as x
struct Node* create_node(int x) {
    struct Node* ptr = malloc(sizeof(struct Node));
    ptr->next = NULL;
    ptr->data = x;
    return ptr;
}

// delete the node at `ptr` and free its memory
void delete_node(struct Node* ptr) {
    free(ptr);
}

// ------------------------------ Node struct definition ends here ------------------------------

// Use this to operate on the list, this will always point at the head of the list.
struct Node* PythonListHead = NULL;


// prints the list in space seperated format
void print_list(struct Node* head) {
    struct Node* cur = head;
    while(cur) {
        printf("%d ", cur->data);
        cur = cur->next;
    }
    printf("\n");
}


// Add an item to the end of the list
void append(int x) {
    struct Node* ptr1=create_node(x);
    if(PythonListHead==NULL){
    PythonListHead = ptr1;
    return;
    }
    struct Node* cur = PythonListHead;
    while(cur) {
        if(cur->next == NULL)
        break;
        cur = cur->next;
    }
    cur->next = ptr1;
}


// Return the number of elements in the list
int len() {
    if(PythonListHead==NULL)
    return 0;
    struct Node* cur = PythonListHead;
    int count=0;
    while(cur) {
        count++;
        cur = cur->next;
    }
    return count;
}

// Insert an item at a given position. 
// The first argument is the index of the element before which to insert
// second argument is the value to insert at that position
// if the position does not exist, do nothing
void insert(int position, int x) {
    if(position>=len())
    return;
    if(position==0)
    {
        struct Node* ptr2=create_node(x);
        ptr2->next = PythonListHead;
        PythonListHead = ptr2;
        return;
    }
    struct Node* cur = PythonListHead;
    for(int i=0;i<position-1;i++){
        cur = cur->next;
    }
    struct Node* ptr1=create_node(x);
    ptr1->next = cur->next;
    cur->next = ptr1;
}


// Remove the item at the end of the list
void pop() {
    if(PythonListHead==NULL)
    return;
    if(len()==1){
        delete_node(PythonListHead);
        PythonListHead = NULL;
        return;
    }
    struct Node* cur = PythonListHead;
    while(cur) {
        if(cur->next->next == NULL)
        break;
        cur = cur->next;
    }
    delete_node(cur->next);
    cur->next = NULL;
}


// Remove all items from the list
void clear() {
    if(PythonListHead==NULL)
    return;
    struct Node* cur = PythonListHead;
    while(cur){
        struct Node* copy;
        copy = cur;
        cur = cur->next;
        delete_node(copy);
    }
    PythonListHead=NULL;
}


// Return the number of times x appears in the list.
int count(int x) {
    // your code goes here
    if(PythonListHead==NULL)
    return 0;
    struct Node* cur = PythonListHead;
    int count=0;
    while(cur) {
        if(x == cur->data)
            count++;
        cur = cur->next;
    }
    return count;
}


// Reverse the elements of the list in place.
// Make sure you change `PythonListHead` accordingly
void reverse() {
    if (len()==0 || len()==1)
    return;
    struct Node* cur = PythonListHead;
    struct Node* after = PythonListHead->next;
    cur->next=NULL;
    struct Node* before = cur;
    cur = after;
    while(cur){
        after=cur->next;
        cur->next=before;
        before=cur;
        cur=after;
    }
    PythonListHead = before;
}




// Set the data attribute of the node at `position` to `x`
// if no such position, do nothing
void setitem(int position, int x) {
    if(PythonListHead==NULL || position>=len())
    return;
    struct Node* cur = PythonListHead;
    int i=0;
    for(int i=0;i<position;i++){
        cur = cur->next;
    }
    cur->data = x;
}


// Return the data of the node at `position` 
// if no such position, return -1
int getitem(int position) {
    if(PythonListHead==NULL || position>=len())
        return -1;
    struct Node* cur = PythonListHead;
    int i=0;
    for(int i=0;i<position;i++){
        cur = cur->next;
    }
    return (cur->data);
}


// erase the node at position
// if no such position, do nothing
void erase(int position) {
    struct Node* cur = PythonListHead;
    if(position>=len())
        return;
    if(position==0)
    {
        PythonListHead = cur->next;
        delete_node(cur);
        return;
    }
    if(PythonListHead==NULL)
        return;
    for(int i=0; i<position-1;i++){
        cur = cur->next;
    }
    struct Node* copy = cur->next->next;
    delete_node(cur->next);
    cur->next = copy;
}


// Returns a the head of the newly formed Python List
// containing elements present in positions in the original List.
// Note: you have to create new Python List and return its head.
// Here positions is an array of size n.
// eg. if positions = [2, 3, 5], you need to return a newly formed list
// having nodes that were at position 2, 3 and 5 in the original list.
// if there is such a position that is not present in the original list, do nothing
// with that position.
struct Node* index_into(int *positions, int n) {
    struct Node* NewHead = NULL;
    struct Node* cur;
    struct Node* ptr;
    for(int i=0;i<n;i++)
    {
        int pos = positions[i];
        if(pos>=len())
            continue;
        int val = getitem(pos);
        ptr=create_node(val);
        if(NewHead == NULL)
        {
            NewHead = ptr;
            cur = ptr;
        }
        else
        {
            cur->next = ptr;
            cur = ptr;
        }
    }
        return NewHead;
}


// swaps the nodes present at `position` and `position+1`
// if either of  `position` or `position+1` does not exist, do nothing
void swap(int position) {
    if(position<0 || position>(len()-2))
    return;
    struct Node* cur = PythonListHead;
    struct Node* temp;
    struct Node* initial = PythonListHead;


    if(position==0)
    {
        cur=PythonListHead;
        temp = cur->next;
        cur->next = temp->next;
        temp->next=cur;
        PythonListHead = temp;
        return;
    }

    if(position==(len()-2))
    {
        for(int i=0;i<position;i++)
        {
            cur = cur->next;
        }
        temp = cur->next;
        cur->next = NULL;
        temp->next=cur;
        for(int j=0;j<position-1;j++){
            initial = initial->next;
        }
        initial->next=temp;
        return;
    }

    for(int i=0;i<position;i++){
        cur = cur->next;
    }
    temp = cur->next;
    cur->next = temp->next;
    temp->next = cur;
    for(int j=0;j<position-1;j++){
        initial = initial->next;
    }
    initial->next=temp;
}


// sort the Python list
// you may use the above defined swap function to 
// implement bubble sort. But its upto you, use whatever algorithm
// that you seem comfortable.
void sort() {
    int n= len();
    if(n==0 || n==1)
        return;
    
    for (int i=0;i<n-1;i++)
    {
        for (int j=0;j<n-i-1;j++)
        {
            if(getitem(j)>getitem(j+1))
            {
                swap(j);
            }
        }
    }
}


// ----------------------- Driver program starts here -----------------------

int main(int argc, char const *argv[])
{
    int T; 
    scanf("%d", &T);

    char operation_type[20];
    int indices[100];

    while(T--) {
        scanf("%s", operation_type);

        if(strcmp(operation_type, "append") == 0) {
            int x;
            scanf("%d", &x);
            append(x);
        } 

        if(strcmp(operation_type, "insert") == 0) {
            int pos, x;
            scanf("%d %d", &pos, &x);
            insert(pos, x);
        }

        if(strcmp(operation_type, "pop") == 0) {
            pop();
        }

        if(strcmp(operation_type, "clear") == 0) {
            clear();
        }

        if(strcmp(operation_type, "count") == 0) {
            int x;
            scanf("%d", &x);
            int cnt = count(x);
            printf("%d\n", cnt);
        }

        if(strcmp(operation_type, "reverse") == 0) {
            reverse();
        }

        if(strcmp(operation_type, "len") == 0) {
            int length = len();
            printf("%d\n", length);
        }

        if(strcmp(operation_type, "setitem") == 0) {
            int pos, x;
            scanf("%d %d", &pos, &x);
            setitem(pos, x);
        }

        if(strcmp(operation_type, "getitem") == 0) {
            int pos;
            scanf("%d", &pos);
            int value = getitem(pos);
            printf("%d\n", value);
        }

        if(strcmp(operation_type, "print") == 0) {
            print_list(PythonListHead);
        }

        if(strcmp(operation_type, "erase") == 0) {
            int pos;
            scanf("%d", &pos);
            erase(pos);
        }

        if(strcmp(operation_type, "swap") == 0) {
            int pos;
            scanf("%d", &pos);
            swap(pos);
        }

        if(strcmp(operation_type, "index_into") == 0) {
            int n;
            scanf("%d", &n);
            for(int i=0;i<n;i++) scanf("%d", &indices[i]);
            struct Node* new_head = index_into(indices, n);
            print_list(new_head);
        }

        if(strcmp(operation_type, "sort") == 0) {
            sort();
        }
    }
}