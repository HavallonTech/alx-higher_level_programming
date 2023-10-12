#ifndef main_h
#define main_h


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct dlistint_s{
	int n;
	struct dlistint_s *next;
	struct dlistint_t *prev;

}dlistint_t;
struct dlistint_s *head = NULL;
struct dlistint_s *current = NULL;
void insertatbegin(int data);
int printList();

#endif
