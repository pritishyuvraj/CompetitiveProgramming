
void func_find_pigeon_hole(){
	int i, j;
	for (i = 0; i< n; i++){
		for(j = 0; j < n; j++){
			if (i != j){
				if (f(i) == f(j)){
					printf("Found diff inputs having same outputs %d %d", i, j);
				}
			}
		}
	}
}