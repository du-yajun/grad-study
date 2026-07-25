for epoch in range(num_epochs):
    for X, y in dataloader:
        y_hat = model(X)
        loss = loss(y_hat, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
