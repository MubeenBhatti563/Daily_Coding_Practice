using System;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;

public class Program
{
    private static readonly HttpClient sharedClient = new()
    {
        BaseAddress = new Uri("https://jsonplaceholder.typicode.com"),
    };

    static async Task Main(string[] args)
    {
        Console.WriteLine("Fetching data from JSONPlaceholder!");

        try
        {
            Post post = await FetchPostAsync("/posts/1");

            if (post != null)
            {
                Console.WriteLine("\n--- Post Details ---");
                Console.WriteLine($"ID: {post.Id}");
                Console.WriteLine($"Title: {post.Title}");
                Console.WriteLine($"User ID: {post.UserId}");
                Console.WriteLine($"Body: {post.Body}");
            }
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"\nError fetching data: {e.Message}");
            Console.WriteLine($"Status code: {e.StatusCode}");
        }
        catch (NotSupportedException)
        {
            Console.WriteLine("\nError: Invalid JSON or unsupported content type.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"\nAn unexpected error occurred: {e.Message}");
        }

        Console.WriteLine("\nProcess finished. Press any key to exit.");
        Console.ReadKey();
    }

    static async Task<Post> FetchPostAsync(string endpointUrl)
    {
        return await sharedClient.GetFromJsonAsync<Post>(endpointUrl);
    }
}

// JSON Model for "posts"
public class Post
{
    public int UserId { get; set; }
    public int Id { get; set; }
    public string Title { get; set; }
    public string Body { get; set; }
}