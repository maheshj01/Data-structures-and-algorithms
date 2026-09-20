class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        
        # recipes depend on supplies
        # adj = {
        #  yeast: [bread]
        #  flour: [bread]
        #  meat: [sandwich],
        #  bread: [sandwich]
        # }
        
        # in degree always represents the required dependencies
        # in_degree = {
        # yeast: 0, 
        # flour: 0,
        # meat: 0,
        #  bread: 0, 
        #  sandwich:1,
        # }
        # q = []
        # result = ["bread"]
        in_degree = defaultdict(int)
        dependencies = defaultdict(list)
       
        for i, recipe in enumerate(recipes):
            in_degree[recipe] = len(ingredients[i])
            for j in range(len(ingredients[i])):
                dependencies[ingredients[i][j]].append(recipe)

        print("dependencies",dependencies, " indegre=", in_degree)

    
        # add supplies to q becasue they have indegree 0
        q = deque([supply for supply in supplies])
        result = []
        while(q):
            supply = q.popleft()
            for recipe in dependencies[supply]:
                in_degree[recipe] -= 1
                if(in_degree[recipe] == 0):
                    # Adding it to queue allows us to check,
                    #  if any recipe depends on this new recipe
                    q.append(recipe)
                    result.append(recipe)
        return result
