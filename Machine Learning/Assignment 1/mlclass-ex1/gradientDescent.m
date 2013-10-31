function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
    sum1 = 0;
    sum2 = 0;
    for iter1 = 1:m
        hx1 = theta(1) + X(iter1, 2) * theta(2);
        sum1 = sum1 + (hx1 - y(iter1));
        sum2 = sum2 + (hx1 - y(iter1)) * X(iter1, 2);
        %temp2 = theta(2) - alpha * sum(hx2(:,2) - y) / m
    % ============================================================
    % Save the cost J in every iteration    
    end
    theta = [theta(1) - (alpha/m) * sum1; theta(2) - (alpha/m) * sum2];
    %temp = X' * (X * theta - y);
    %theta = theta - (alpha / m) * temp;
    J_history(iter) = computeCost(X, y, theta);
end

end
