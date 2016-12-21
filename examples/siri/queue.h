#ifndef _QUEUE_LIST_H  
#define _QUEUE_LIST_H  
  
#define ElementType int  
struct Node;  
struct QNode;  
typedef struct Node *PtrToNode;  
typedef PtrToNode Queue;  
  
  
int IsEmpty( Queue Q );  
Queue CreateQueue( void );  
void DisposeQueue( Queue Q );  
void MakeEmpty( Queue Q );  
void Enqueue( ElementType X, Queue Q );  
ElementType Head( Queue Q );  
void Dequeue( Queue Q );  
ElementType FrontAndDequeue( Queue Q );  
  
Queue Q = CreateQueue();

#endif /* _QUEUE_LIST_H */  
