
import useSWR from 'swr';

const API_BASE_URL = 'http://127.0.0.1:8000';

// A simple fetcher function that returns the JSON data.
const fetcher = (url: string) => fetch(url).then((res) => res.json());

interface ApiQueryData {
  path: string;
  options?: Record<string, unknown>;
  autoInit?: boolean;
}

export const useApiQuery = ({ path, options, autoInit = true }: ApiQueryData) => {
  const fullPath = `${API_BASE_URL}${path}`;

  const { data, error, mutate } = useSWR(autoInit ? fullPath : null, fetcher, {
    revalidateIfStale: true,
    revalidateOnFocus: false,
    revalidateOnReconnect: true,
    ...options,
  });

  return {
    data: data,
    isLoading: !error && !data,
    isError: error,
    mutate: mutate,
  };
};
